import Link from "next/link"
import Navbar from "../components/Navbar";

export default function About() {
    return (
        <div className="bg-slate-800 h-screen flex flex-col overflow-x-hidden">
            <Navbar/>

            <div className="flex-1 bg-gray-900 text-white flex flex-col items-center justify-center px-4 py-16">
                <div className="flex flex-wrap justify-center gap-6 mb-10">
                <div className="bg-gray-800 w-60 h-32 flex items-center justify-center rounded-lg">
                    <p className="text-lg font-bold">Aaron Medina</p>
                </div>
                <div className="bg-gray-800 w-60 h-32 flex items-center justify-center rounded-lg">
                    <p className="text-lg font-bold">Aleksander Mazey</p>
                </div>
                <div className="bg-gray-800 w-60 h-32 flex items-center justify-center rounded-lg">
                    <div className="items-center justify-center">
                        <p className="text-lg font-bold">Uchechi Ndubueze</p>
                        <p className="text-lg font-bold">(Precious)</p> 
                    </div>
                </div>
                <div className="bg-gray-800 w-60 h-32 flex items-center justify-center rounded-lg">
                    <p className="text-lg font-bold">Victoria Bayang</p>
                </div>
                </div>
            </div>

            <footer className="text-center py-6 bg-gray-800">
                <p className="text-gray-400">2024 Volunteer Webpage - UH Software Design 4353</p>
            </footer>

        </div>
    );
}
   
