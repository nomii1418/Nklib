import { useState, useEffect } from 'react';
import { useAuth } from '../context/AuthContext';
import { useNavigate } from 'react-router-dom';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '../components/ui/tabs';
import { Card, CardContent, CardHeader, CardTitle } from '../components/ui/card';
import { Button } from '../components/ui/button';
import { Input } from '../components/ui/input';
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogDescription } from '../components/ui/dialog';
import { Progress } from '../components/ui/progress';
import { 
  getSubjects, createSubject, updateSubject, deleteSubject,
  getTopics, createTopic, updateTopic, deleteTopic,
  createVideo, updateVideo, deleteVideo,
  createFile, updateFile, deleteFile,
  createQuiz, updateQuiz, deleteQuiz,
  createTip, updateTip, deleteTip
} from '../services/api';
import { Plus, Edit, Trash2, Upload, BookOpen, Video, FileText, Award, Lightbulb } from 'lucide-react';

export const Admin = () => {
  const { isAdmin } = useAuth();
  const navigate = useNavigate();
  const [subjects, setSubjects] = useState<any[]>([]);
  const [selectedSubject, setSelectedSubject] = useState<string>('');
  const [showDialog, setShowDialog] = useState(false);
  const [dialogType, setDialogType] = useState<'subject' | 'topic' | 'video' | 'file' | 'quiz' | 'tip'>('subject');
  const [formData, setFormData] = useState<any>({});
  const [uploadProgress, setUploadProgress] = useState(0);
  const [uploading, setUploading] = useState(false);
  const [refresh, setRefresh] = useState(0);

  useEffect(() => {
    if (!isAdmin) {
      navigate('/');
      return;
    }
    loadSubjects();
  }, [isAdmin, navigate, refresh]);

  const loadSubjects = async () => {
    try {
      const data = await getSubjects();
      setSubjects(data);
    } catch (error) {
      console.error('Failed to load subjects:', error);
    }
  };

  const handleCreateSubject = () => {
    setDialogType('subject');
    setFormData({});
    setShowDialog(true);
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    try {
      const formDataObj = new FormData();
      
      if (dialogType === 'subject') {
        formDataObj.append('name', formData.name || '');
        formDataObj.append('description', formData.description || '');
        formDataObj.append('icon', formData.icon || '');
        formDataObj.append('order', formData.order || '0');
        
        if (formData._id) {
          await updateSubject(formData._id, formDataObj);
        } else {
          await createSubject(formDataObj);
        }
      } else if (dialogType === 'topic') {
        formDataObj.append('subject_id', selectedSubject);
        formDataObj.append('name', formData.name || '');
        formDataObj.append('description', formData.description || '');
        formDataObj.append('order', formData.order || '0');
        
        if (formData._id) {
          await updateTopic(formData._id, formDataObj);
        } else {
          await createTopic(formDataObj);
        }
      } else if (dialogType === 'video') {
        formDataObj.append('subject_id', selectedSubject);
        formDataObj.append('topic_id', formData.topic_id || '');
        formDataObj.append('title', formData.title || '');
        formDataObj.append('description', formData.description || '');
        formDataObj.append('url', formData.url || '');
        formDataObj.append('thumbnail', formData.thumbnail || '');
        formDataObj.append('duration', formData.duration || '');
        formDataObj.append('order', formData.order || '0');
        
        if (formData._id) {
          await updateVideo(formData._id, formDataObj);
        } else {
          await createVideo(formDataObj);
        }
      } else if (dialogType === 'file') {
        setUploading(true);
        formDataObj.append('subject_id', selectedSubject);
        formDataObj.append('topic_id', formData.topic_id || '');
        formDataObj.append('title', formData.title || '');
        formDataObj.append('description', formData.description || '');
        formDataObj.append('order', formData.order || '0');
        
        if (formData.file) {
          formDataObj.append('file', formData.file);
        }
        
        if (formData._id) {
          await updateFile(formData._id, formDataObj, setUploadProgress);
        } else {
          await createFile(formDataObj, setUploadProgress);
        }
        setUploading(false);
      } else if (dialogType === 'quiz') {
        formDataObj.append('subject_id', selectedSubject);
        formDataObj.append('topic_id', formData.topic_id || '');
        formDataObj.append('title', formData.title || '');
        formDataObj.append('description', formData.description || '');
        formDataObj.append('questions', JSON.stringify(formData.questions || []));
        formDataObj.append('duration', formData.duration || '');
        formDataObj.append('order', formData.order || '0');
        
        if (formData._id) {
          await updateQuiz(formData._id, formDataObj);
        } else {
          await createQuiz(formDataObj);
        }
      } else if (dialogType === 'tip') {
        formDataObj.append('subject_id', selectedSubject);
        formDataObj.append('topic_id', formData.topic_id || '');
        formDataObj.append('title', formData.title || '');
        formDataObj.append('content', formData.content || '');
        formDataObj.append('order', formData.order || '0');
        
        if (formData._id) {
          await updateTip(formData._id, formDataObj);
        } else {
          await createTip(formDataObj);
        }
      }
      
      setShowDialog(false);
      setFormData({});
      setUploadProgress(0);
      setRefresh(prev => prev + 1);
    } catch (error) {
      console.error('Failed to submit:', error);
      alert('Failed to save. Please try again.');
    }
  };

  const handleDelete = async (type: string, id: string) => {
    if (!confirm('Are you sure you want to delete this item?')) return;
    
    try {
      if (type === 'subject') await deleteSubject(id);
      else if (type === 'topic') await deleteTopic(id);
      else if (type === 'video') await deleteVideo(id);
      else if (type === 'file') await deleteFile(id);
      else if (type === 'quiz') await deleteQuiz(id);
      else if (type === 'tip') await deleteTip(id);
      
      setRefresh(prev => prev + 1);
    } catch (error) {
      console.error('Failed to delete:', error);
      alert('Failed to delete. Please try again.');
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="mb-8">
          <h1 className="text-4xl font-bold text-gray-900 mb-2">Admin Panel</h1>
          <p className="text-gray-600">Manage all platform content</p>
        </div>

        <Tabs defaultValue="subjects">
          <TabsList className="grid grid-cols-6 w-full max-w-3xl">
            <TabsTrigger value="subjects">
              <BookOpen className="h-4 w-4 mr-2" />
              Subjects
            </TabsTrigger>
            <TabsTrigger value="topics">Topics</TabsTrigger>
            <TabsTrigger value="videos">
              <Video className="h-4 w-4 mr-2" />
              Videos
            </TabsTrigger>
            <TabsTrigger value="files">
              <FileText className="h-4 w-4 mr-2" />
              Files
            </TabsTrigger>
            <TabsTrigger value="quizzes">
              <Award className="h-4 w-4 mr-2" />
              Quizzes
            </TabsTrigger>
            <TabsTrigger value="tips">
              <Lightbulb className="h-4 w-4 mr-2" />
              Tips
            </TabsTrigger>
          </TabsList>

          <TabsContent value="subjects" className="space-y-4 mt-6">
            <div className="flex justify-between items-center">
              <h2 className="text-2xl font-semibold">Subjects</h2>
              <Button onClick={handleCreateSubject}>
                <Plus className="h-4 w-4 mr-2" />
                Add Subject
              </Button>
            </div>
            
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {subjects.map((subject) => (
                <Card key={subject._id}>
                  <CardHeader>
                    <CardTitle className="text-lg flex items-center justify-between">
                      <span>{subject.icon} {subject.name}</span>
                      <div className="flex space-x-2">
                        <Button size="sm" variant="ghost" onClick={() => {
                          setDialogType('subject');
                          setFormData(subject);
                          setShowDialog(true);
                        }}>
                          <Edit className="h-4 w-4" />
                        </Button>
                        <Button size="sm" variant="ghost" onClick={() => handleDelete('subject', subject._id)}>
                          <Trash2 className="h-4 w-4 text-red-500" />
                        </Button>
                      </div>
                    </CardTitle>
                  </CardHeader>
                  <CardContent>
                    <p className="text-sm text-gray-600">{subject.description}</p>
                  </CardContent>
                </Card>
              ))}
            </div>
          </TabsContent>

          <TabsContent value="topics" className="space-y-4 mt-6">
            <div className="flex justify-between items-center">
              <h2 className="text-2xl font-semibold">Topics</h2>
              <div className="flex space-x-4">
                <select 
                  className="border rounded-md px-3 py-2"
                  value={selectedSubject}
                  onChange={(e) => setSelectedSubject(e.target.value)}
                >
                  <option value="">Select Subject</option>
                  {subjects.map(s => (
                    <option key={s._id} value={s._id}>{s.name}</option>
                  ))}
                </select>
                <Button onClick={() => {
                  if (!selectedSubject) {
                    alert('Please select a subject first');
                    return;
                  }
                  setDialogType('topic');
                  setFormData({});
                  setShowDialog(true);
                }}>
                  <Plus className="h-4 w-4 mr-2" />
                  Add Topic
                </Button>
              </div>
            </div>
            <p className="text-gray-600">Select a subject to manage its topics</p>
          </TabsContent>

          {/* Similar tabs for videos, files, quizzes, and tips */}
        </Tabs>

        {/* Dialog for Add/Edit */}
        <Dialog open={showDialog} onOpenChange={setShowDialog}>
          <DialogContent className="max-w-2xl max-h-[80vh] overflow-y-auto">
            <DialogHeader>
              <DialogTitle>
                {formData._id ? 'Edit' : 'Add'} {dialogType.charAt(0).toUpperCase() + dialogType.slice(1)}
              </DialogTitle>
              <DialogDescription>
                Fill in the details below
              </DialogDescription>
            </DialogHeader>
            
            <form onSubmit={handleSubmit} className="space-y-4">
              {dialogType === 'subject' && (
                <>
                  <div>
                    <label className="text-sm font-medium">Name</label>
                    <Input
                      value={formData.name || ''}
                      onChange={(e) => setFormData({...formData, name: e.target.value})}
                      required
                    />
                  </div>
                  <div>
                    <label className="text-sm font-medium">Description</label>
                    <Input
                      value={formData.description || ''}
                      onChange={(e) => setFormData({...formData, description: e.target.value})}
                      required
                    />
                  </div>
                  <div>
                    <label className="text-sm font-medium">Icon (emoji)</label>
                    <Input
                      value={formData.icon || ''}
                      onChange={(e) => setFormData({...formData, icon: e.target.value})}
                    />
                  </div>
                </>
              )}
              
              {dialogType === 'file' && (
                <>
                  <div>
                    <label className="text-sm font-medium">Title</label>
                    <Input
                      value={formData.title || ''}
                      onChange={(e) => setFormData({...formData, title: e.target.value})}
                      required
                    />
                  </div>
                  <div>
                    <label className="text-sm font-medium">Description</label>
                    <Input
                      value={formData.description || ''}
                      onChange={(e) => setFormData({...formData, description: e.target.value})}
                      required
                    />
                  </div>
                  <div>
                    <label className="text-sm font-medium">File</label>
                    <Input
                      type="file"
                      onChange={(e) => setFormData({...formData, file: e.target.files?.[0]})}
                      required={!formData._id}
                    />
                  </div>
                  {uploading && (
                    <div>
                      <Progress value={uploadProgress} />
                      <p className="text-sm text-center mt-2">{uploadProgress}% uploaded</p>
                    </div>
                  )}
                </>
              )}
              
              <div className="flex justify-end space-x-2">
                <Button type="button" variant="outline" onClick={() => setShowDialog(false)}>
                  Cancel
                </Button>
                <Button type="submit" disabled={uploading}>
                  {uploading ? 'Uploading...' : 'Save'}
                </Button>
              </div>
            </form>
          </DialogContent>
        </Dialog>
      </div>
    </div>
  );
};
