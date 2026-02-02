import { NextRequest, NextResponse } from 'next/server';
import { cookies } from 'next/headers';

export async function POST(request: NextRequest) {
  try {
    const { email, password } = await request.json();

    // Get the backend API URL from environment variables
    const apiUrl = process.env.NEXT_PUBLIC_BETTER_AUTH_URL;
    if (!apiUrl) {
      throw new Error('Backend API URL is not configured.');
    }
    const loginUrl = `${apiUrl}/auth/login`;

    // Forward the login request to the actual backend
    const apiResponse = await fetch(loginUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ email, password }),
    });

    const data = await apiResponse.json();

    if (!apiResponse.ok) {
      // If the backend returned an error, forward it to the client
      return NextResponse.json(data, { status: apiResponse.status });
    }

    // On successful login, extract the token and set it in a secure, HttpOnly cookie
    const token = data.access_token;
    if (token) {
      const cookieStore = cookies();
      
      // Set the cookie
      cookieStore.set('better-auth.session_token', token, {
        httpOnly: true, // Makes the cookie inaccessible to client-side JS
        secure: process.env.NODE_ENV === 'production', // Use secure cookies in production
        path: '/', // Accessible across the entire site
        sameSite: 'lax', // Or 'strict' for better security
        maxAge: 60 * 60 * 24 * 7, // 7 days
      });

      return NextResponse.json({ success: true }, { status: 200 });
    } else {
      // If the backend response was successful but had no token
      return NextResponse.json({ error: 'Authentication successful, but no token was provided.' }, { status: 500 });
    }

  } catch (error) {
    console.error('API Route /api/auth/login Error:', error);
    return NextResponse.json({ error: 'An internal server error occurred.' }, { status: 500 });
  }
}
