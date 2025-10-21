import { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import { getSubject, getSubjectContent } from '../services/api';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '../components/ui/card';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '../components/ui/tabs';
import { Button } from '../components/ui/button';
import { Video, FileText, Award, Lightbulb, Download, ExternalLink, BookOpen, ArrowLeft } from 'lucide-react';

interface Subject {
  _id: string;
  name: string;
  description: string;
}

interface Content {
  topics: any[];
  videos: any[];
  files: any[];
  quizzes: any[];
  tips: any[];
}

export const SubjectDetail = () => {
  const { id } = useParams<{ id: string }>();
  const [subject, setSubject] = useState<Subject | null>(null);
  const [content, setContent] = useState<Content | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadData();
  }, [id]);

  const loadData = async () => {
    try {
      const [subjectData, contentData] = await Promise.all([
        getSubject(id!),
        getSubjectContent(id!)
      ]);
      setSubject(subjectData);
      setContent(contentData);
    } catch (error) {
      console.error('Failed to load data:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary mx-auto"></div>
          <p className="mt-4 text-gray-600">Loading content...</p>
        </div>
      </div>
    );
  }

  if (!subject || !content) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <Card>
          <CardContent className="py-12 text-center">
            <p className="text-gray-600">Subject not found</p>
            <Link to="/subjects">
              <Button className="mt-4">Back to Subjects</Button>
            </Link>
          </CardContent>
        </Card>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <Link to="/subjects">
          <Button variant="ghost" className="mb-6">
            <ArrowLeft className="h-4 w-4 mr-2" />
            Back to Subjects
          </Button>
        </Link>

        <div className="mb-8">
          <h1 className="text-4xl font-bold text-gray-900 mb-4">{subject.name}</h1>
          <p className="text-xl text-gray-600">{subject.description}</p>
        </div>

        <Tabs defaultValue="topics" className="space-y-6">
          <TabsList className="grid grid-cols-5 w-full max-w-3xl">
            <TabsTrigger value="topics">
              <BookOpen className="h-4 w-4 mr-2" />
              Topics ({content.topics.length})
            </TabsTrigger>
            <TabsTrigger value="videos">
              <Video className="h-4 w-4 mr-2" />
              Videos ({content.videos.length})
            </TabsTrigger>
            <TabsTrigger value="files">
              <FileText className="h-4 w-4 mr-2" />
              Files ({content.files.length})
            </TabsTrigger>
            <TabsTrigger value="quizzes">
              <Award className="h-4 w-4 mr-2" />
              Quizzes ({content.quizzes.length})
            </TabsTrigger>
            <TabsTrigger value="tips">
              <Lightbulb className="h-4 w-4 mr-2" />
              Tips ({content.tips.length})
            </TabsTrigger>
          </TabsList>

          <TabsContent value="topics" className="space-y-4">
            {content.topics.length === 0 ? (
              <Card>
                <CardContent className="py-12 text-center text-gray-600">
                  No topics available yet
                </CardContent>
              </Card>
            ) : (
              content.topics.map((topic) => (
                <Link key={topic._id} to={`/topics/${topic._id}`}>
                  <Card className="hover:shadow-md transition-shadow cursor-pointer">
                    <CardHeader>
                      <CardTitle>{topic.name}</CardTitle>
                      <CardDescription>{topic.description}</CardDescription>
                    </CardHeader>
                  </Card>
                </Link>
              ))
            )}
          </TabsContent>

          <TabsContent value="videos" className="space-y-4">
            {content.videos.length === 0 ? (
              <Card>
                <CardContent className="py-12 text-center text-gray-600">
                  No videos available yet
                </CardContent>
              </Card>
            ) : (
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {content.videos.map((video) => (
                  <Card key={video._id}>
                    <CardHeader>
                      <CardTitle className="flex items-center justify-between">
                        <span>{video.title}</span>
                        <Video className="h-5 w-5 text-primary" />
                      </CardTitle>
                      <CardDescription>{video.description}</CardDescription>
                    </CardHeader>
                    <CardContent>
                      <a href={video.url} target="_blank" rel="noopener noreferrer">
                        <Button className="w-full">
                          <ExternalLink className="h-4 w-4 mr-2" />
                          Watch Video
                        </Button>
                      </a>
                    </CardContent>
                  </Card>
                ))}
              </div>
            )}
          </TabsContent>

          <TabsContent value="files" className="space-y-4">
            {content.files.length === 0 ? (
              <Card>
                <CardContent className="py-12 text-center text-gray-600">
                  No files available yet
                </CardContent>
              </Card>
            ) : (
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {content.files.map((file) => (
                  <Card key={file._id}>
                    <CardHeader>
                      <CardTitle className="flex items-center justify-between">
                        <span>{file.title}</span>
                        <FileText className="h-5 w-5 text-primary" />
                      </CardTitle>
                      <CardDescription>{file.description}</CardDescription>
                    </CardHeader>
                    <CardContent>
                      <div className="text-sm text-gray-600 mb-4">
                        Size: {(file.file_size / 1024).toFixed(2)} KB
                      </div>
                      <a href={`http://localhost:8000${file.download_url}`} download>
                        <Button className="w-full">
                          <Download className="h-4 w-4 mr-2" />
                          Download File
                        </Button>
                      </a>
                    </CardContent>
                  </Card>
                ))}
              </div>
            )}
          </TabsContent>

          <TabsContent value="quizzes" className="space-y-4">
            {content.quizzes.length === 0 ? (
              <Card>
                <CardContent className="py-12 text-center text-gray-600">
                  No quizzes available yet
                </CardContent>
              </Card>
            ) : (
              content.quizzes.map((quiz) => (
                <Card key={quiz._id}>
                  <CardHeader>
                    <CardTitle className="flex items-center justify-between">
                      <span>{quiz.title}</span>
                      <Award className="h-5 w-5 text-primary" />
                    </CardTitle>
                    <CardDescription>{quiz.description}</CardDescription>
                  </CardHeader>
                  <CardContent>
                    <div className="text-sm text-gray-600 mb-4">
                      {quiz.questions.length} Questions
                      {quiz.duration && ` • ${quiz.duration} minutes`}
                    </div>
                    <Button className="w-full">Start Quiz</Button>
                  </CardContent>
                </Card>
              ))
            )}
          </TabsContent>

          <TabsContent value="tips" className="space-y-4">
            {content.tips.length === 0 ? (
              <Card>
                <CardContent className="py-12 text-center text-gray-600">
                  No tips available yet
                </CardContent>
              </Card>
            ) : (
              content.tips.map((tip) => (
                <Card key={tip._id}>
                  <CardHeader>
                    <CardTitle className="flex items-center">
                      <Lightbulb className="h-5 w-5 text-yellow-500 mr-2" />
                      {tip.title}
                    </CardTitle>
                  </CardHeader>
                  <CardContent>
                    <p className="text-gray-700 whitespace-pre-wrap">{tip.content}</p>
                  </CardContent>
                </Card>
              ))
            )}
          </TabsContent>
        </Tabs>
      </div>
    </div>
  );
};
