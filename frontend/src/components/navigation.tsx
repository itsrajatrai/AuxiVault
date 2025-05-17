export default function Header() {
    return (
      <header className="bg-white shadow-md fixed top-0 left-0 right-0 z-50">
        <div className="container mx-auto flex justify-between items-center p-4">
  
          {/* Left: Logo */}
          <div className="flex items-center space-x-2"> 
            AuxiVault
          </div>
  
          {/* Center: Nav Links  with nav have a bnorder rounded*/}
          <nav className="flex space-x-20 border rounded-4xl p-4 bg-gray-50">
            <a href="#" className="text-gray-700 hover:text-blue-600 font-medium">Home</a>
            <a href="#" className="text-gray-700 hover:text-blue-600 font-medium">Features</a>
            <a href="#" className="text-gray-700 hover:text-blue-600 font-medium">Pricing</a>
            <a href="#" className="text-gray-700 hover:text-blue-600 font-medium">About</a>
            <a href="#" className="text-gray-700 hover:text-blue-600 font-medium">Contact</a>
          </nav>
  
          {/* Right: Login/Register */}
          <div className="flex items-center space-x-4">
            <button className="px-4 py-2 text-blue-600 font-semibold hover:underline">Login/Register</button>
          </div>
  
        </div>
      </header>
    );
  }
  