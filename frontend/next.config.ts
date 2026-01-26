import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  experimental: {
    turbo: {
      // Disable Turbopack for stability
      enabled: false
    }
  }
};

export default nextConfig;
