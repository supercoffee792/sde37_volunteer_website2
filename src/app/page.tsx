import Image from "next/image";
import Link from "next/link";
import Navbar from "./components/Navbar";

export default function Home() {
  return (
    <div className="bg-gradient-to-br from-gray-900 via-blue-950 to-blue-900 h-screen flex flex-col overflow-x-hidden">
      <Navbar/>
      
      <div className="flex-1 bg-transparent text-white flex flex-col items-center justify-center px-4 py-16">
        <h2 className="text-4xl font-semibold mb-10 text-gray-100">Make a Difference</h2>
        
        <div className="flex flex-wrap justify-center gap-6">
          <div className="bg-gray-900/30 backdrop-blur-sm border border-gray-800/30 w-72 h-96 flex flex-col items-center justify-center rounded-lg p-4">
            <p className="text-2xl font-bold mb-2 text-gray-100">Manage</p>
            <p className="text-center text-sm text-gray-300">
              Use our simplistic system to manage your events, details, and swiftly notify volunteers of updates.
            </p>
          </div>

          <div className="bg-gray-900/30 backdrop-blur-sm border border-gray-800/30 w-72 h-96 flex flex-col items-center justify-center rounded-lg p-4">
            <p className="text-2xl font-bold mb-2 text-gray-100">Contribute</p>
            <p className="text-center text-sm text-gray-300">
              Support causes you care about and foster growth in your local communities
            </p>
          </div>

          <div className="bg-gray-900/30 backdrop-blur-sm border border-gray-800/30 w-72 h-96 flex flex-col items-center justify-center rounded-lg p-4">
            <p className="text-2xl font-bold mb-2 text-gray-100">Volunteer</p>
            <p className="text-center text-sm text-gray-300">
              Find events that match your skillset and fully make use of your unique talents.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}