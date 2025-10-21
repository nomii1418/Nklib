import { Link } from 'react-router-dom';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '../components/ui/card';
import { Button } from '../components/ui/button';
import { BookOpen, Video, FileText, Brain, Award, Lightbulb } from 'lucide-react';

export const Home = () => {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      {/* Hero Section */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
        <div className="text-center">
          <h1 className="text-5xl font-extrabold text-gray-900 mb-6">
            Welcome to Mechanical Engineering Library
          </h1>
          <p className="text-xl text-gray-600 mb-8 max-w-3xl mx-auto">
            Your comprehensive resource for mechanical engineering education. 
            Access free video tutorials, study materials, quizzes, and AI-powered assistance.
          </p>
          <div className="flex justify-center space-x-4">
            <Link to="/subjects">
              <Button size="lg" className="text-lg px-8">
                Explore Subjects
              </Button>
            </Link>
            <Link to="/ai-assistant">
              <Button size="lg" variant="outline" className="text-lg px-8">
                Try AI Assistant
              </Button>
            </Link>
          </div>
        </div>
      </div>

      {/* Features Section */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <h2 className="text-3xl font-bold text-center text-gray-900 mb-12">
          What We Offer
        </h2>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <Card className="hover:shadow-lg transition-shadow">
            <CardHeader>
              <Video className="h-12 w-12 text-primary mb-4" />
              <CardTitle>Video Tutorials</CardTitle>
              <CardDescription>
                High-quality video lectures covering all major topics in mechanical engineering
              </CardDescription>
            </CardHeader>
          </Card>

          <Card className="hover:shadow-lg transition-shadow">
            <CardHeader>
              <FileText className="h-12 w-12 text-primary mb-4" />
              <CardTitle>Study Materials</CardTitle>
              <CardDescription>
                Comprehensive notes, PDFs, and reference materials for in-depth learning
              </CardDescription>
            </CardHeader>
          </Card>

          <Card className="hover:shadow-lg transition-shadow">
            <CardHeader>
              <Award className="h-12 w-12 text-primary mb-4" />
              <CardTitle>Practice Quizzes</CardTitle>
              <CardDescription>
                Test your knowledge with interactive quizzes and assessments
              </CardDescription>
            </CardHeader>
          </Card>

          <Card className="hover:shadow-lg transition-shadow">
            <CardHeader>
              <Lightbulb className="h-12 w-12 text-primary mb-4" />
              <CardTitle>Tips & Tricks</CardTitle>
              <CardDescription>
                Expert tips and shortcuts to master complex engineering concepts
              </CardDescription>
            </CardHeader>
          </Card>

          <Card className="hover:shadow-lg transition-shadow">
            <CardHeader>
              <Brain className="h-12 w-12 text-primary mb-4" />
              <CardTitle>AI Assistant</CardTitle>
              <CardDescription>
                Get instant answers to your questions with our AI-powered assistant
              </CardDescription>
            </CardHeader>
          </Card>

          <Card className="hover:shadow-lg transition-shadow">
            <CardHeader>
              <BookOpen className="h-12 w-12 text-primary mb-4" />
              <CardTitle>Free Access</CardTitle>
              <CardDescription>
                All content is completely free and accessible to everyone
              </CardDescription>
            </CardHeader>
          </Card>
        </div>
      </div>

      {/* Subjects Preview */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <h2 className="text-3xl font-bold text-center text-gray-900 mb-12">
          Popular Subjects
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {[
            'Thermodynamics',
            'Fluid Mechanics',
            'Machine Design',
            'Manufacturing',
            'Strength of Materials',
            'Heat Transfer',
            'Dynamics',
            'CAD/CAM'
          ].map((subject) => (
            <Card key={subject} className="hover:shadow-lg transition-shadow cursor-pointer">
              <CardHeader>
                <CardTitle className="text-lg">{subject}</CardTitle>
              </CardHeader>
            </Card>
          ))}
        </div>
        <div className="text-center mt-8">
          <Link to="/subjects">
            <Button size="lg" variant="outline">
              View All Subjects
            </Button>
          </Link>
        </div>
      </div>

      {/* Telegram Bot CTA */}
      <div className="bg-primary text-white py-16">
        <div className="max-w-4xl mx-auto text-center px-4">
          <h2 className="text-3xl font-bold mb-4">
            Access via Telegram Bot
          </h2>
          <p className="text-xl mb-8">
            Get instant access to all resources through our powerful Telegram bot. 
            Upload files, manage content, and learn on the go!
          </p>
          <Button size="lg" variant="secondary" className="text-lg px-8">
            Start Using Bot
          </Button>
        </div>
      </div>
    </div>
  );
};
