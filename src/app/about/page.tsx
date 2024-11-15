// import Link from "next/link"
// import Navbar from "../components/Navbar";

// export default function About() {
//     return (
//         <div className="bg-gradient-to-br from-gray-900 via-blue-950 to-blue-900 h-screen flex flex-col overflow-x-hidden">
//             <Navbar/>

//             <div className="flex-1 bg-gray-900 text-white flex flex-col items-center justify-center px-4 py-16">
//                 <div className="flex flex-wrap justify-center gap-6 mb-10">
//                 <div className="bg-gray-800 w-60 h-32 flex items-center justify-center rounded-lg">
//                     <p className="text-lg font-bold">Aaron Medina</p>
//                 </div>
//                 <div className="bg-gray-800 w-60 h-32 flex items-center justify-center rounded-lg">
//                     <p className="text-lg font-bold">Aleksander Mazey</p>
//                 </div>
//                 <div className="bg-gray-800 w-60 h-32 flex items-center justify-center rounded-lg">
//                     <div className="items-center justify-center">
//                         <p className="text-lg font-bold">Uchechi Ndubueze</p>
//                         <p className="text-lg font-bold">(Precious)</p> 
//                     </div>
//                 </div>
//                 <div className="bg-gray-800 w-60 h-32 flex items-center justify-center rounded-lg">
//                     <p className="text-lg font-bold">Victoria Bayang</p>
//                 </div>
//                 </div>
//             </div>

//             <footer className="text-center py-6 bg-gray-800">
//                 <p className="text-gray-400">2024 Volunteer Webpage - UH Software Design 4353</p>
//             </footer>

//         </div>
//     );
// }
   
import Link from "next/link"
import Navbar from "../components/Navbar";

export default function About() {
    return (
        <div className="bg-gradient-to-br from-gray-900 via-blue-950 to-blue-900 h-screen flex flex-col overflow-x-hidden">
            <Navbar/>

            <div className="flex-1 bg-transparent text-white flex flex-col items-center justify-center px-4 py-16">
                <div className="flex flex-wrap justify-center gap-6 mb-10">
                    <div className="bg-gray-900/30 backdrop-blur-sm border border-gray-800/30 w-60 h-32 flex items-center justify-center rounded-lg">
                        <p className="text-lg font-bold text-gray-100">Aaron Medina</p>
                    </div>
                    <div className="bg-gray-900/30 backdrop-blur-sm border border-gray-800/30 w-60 h-32 flex items-center justify-center rounded-lg">
                        <p className="text-lg font-bold text-gray-100">Aleksander Mazey</p>
                    </div>
                    <div className="bg-gray-900/30 backdrop-blur-sm border border-gray-800/30 w-60 h-32 flex items-center justify-center rounded-lg">
                        <div className="items-center justify-center">
                            <p className="text-lg font-bold text-gray-100">Uchechi Ndubueze</p>
                            <p className="text-lg font-bold text-gray-100">(Precious)</p> 
                        </div>
                    </div>
                    <div className="bg-gray-900/30 backdrop-blur-sm border border-gray-800/30 w-60 h-32 flex items-center justify-center rounded-lg">
                        <p className="text-lg font-bold text-gray-100">Victoria Bayang</p>
                    </div>
                </div>
            </div>

            <footer className="text-center py-6 bg-gray-900/50 backdrop-blur-sm border-t border-gray-800/30">
                <p className="text-gray-400">2024 Volunteer Webpage - UH Software Design 4353</p>
            </footer>
        </div>
    );
}