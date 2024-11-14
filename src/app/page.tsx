import Image from "next/image";
import Link from "next/link";
import Navbar from "./components/Navbar";

export default function Home() {
  return (
    <div className="bg-slate-800 h-screen flex flex-col overflow-x-hidden">

      <Navbar/>

      <div className="flex-1 bg-gray-900 text-white flex flex-col items-center justify-center px-4 py-16">
        <h2 className="text-4xl font-semibold mb-10">Make a Difference</h2>
        
        <div className="flex flex-wrap justify-center gap-6">
          <div className="bg-gray-800 w-72 h-96 flex flex-col items-center justify-center rounded-lg p-4">
            <p className="text-2xl font-bold mb-2">Manage</p>
            <p className="text-center text-sm">
              Use our simplistic system to manage your events, details, and swiftly notify volunteers of updates.
            </p>
          </div>

          <div className="bg-gray-800 w-72 h-96 flex flex-col items-center justify-center rounded-lg p-4">
            <p className="text-2xl font-bold mb-2">Contribute</p>
            <p className="text-center text-sm">
              Support causes you care about and foster growth in your local communities
            </p>
          </div>

          <div className="bg-gray-800 w-72 h-96 flex flex-col items-center justify-center rounded-lg p-4">
            <p className="text-2xl font-bold mb-2">Volunteer</p>
            <p className="text-center text-sm">
              Find events that match your skillset and fully make use of your unique talents.
            </p>
          </div>
        </div>

      </div>

    </div>
  );
}
