import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
});

// Add auth token to requests
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Auth
export const login = async (username: string, password: string) => {
  const response = await api.post('/api/auth/login', { username, password });
  return response.data;
};

// Subjects
export const getSubjects = async () => {
  const response = await api.get('/api/subjects');
  return response.data;
};

export const getSubject = async (id: string) => {
  const response = await api.get(`/api/subjects/${id}`);
  return response.data;
};

export const getSubjectContent = async (id: string) => {
  const response = await api.get(`/api/subjects/${id}/content`);
  return response.data;
};

export const createSubject = async (data: FormData) => {
  const response = await api.post('/api/admin/subjects', data);
  return response.data;
};

export const updateSubject = async (id: string, data: FormData) => {
  const response = await api.put(`/api/admin/subjects/${id}`, data);
  return response.data;
};

export const deleteSubject = async (id: string) => {
  const response = await api.delete(`/api/admin/subjects/${id}`);
  return response.data;
};

// Topics
export const getTopics = async (subjectId: string) => {
  const response = await api.get(`/api/subjects/${subjectId}/topics`);
  return response.data;
};

export const getTopic = async (id: string) => {
  const response = await api.get(`/api/topics/${id}`);
  return response.data;
};

export const getTopicContent = async (id: string) => {
  const response = await api.get(`/api/topics/${id}/content`);
  return response.data;
};

export const createTopic = async (data: FormData) => {
  const response = await api.post('/api/admin/topics', data);
  return response.data;
};

export const updateTopic = async (id: string, data: FormData) => {
  const response = await api.put(`/api/admin/topics/${id}`, data);
  return response.data;
};

export const deleteTopic = async (id: string) => {
  const response = await api.delete(`/api/admin/topics/${id}`);
  return response.data;
};

// Videos
export const getVideos = async (subjectId?: string, topicId?: string) => {
  const params = new URLSearchParams();
  if (subjectId) params.append('subject_id', subjectId);
  if (topicId) params.append('topic_id', topicId);
  const response = await api.get(`/api/videos?${params.toString()}`);
  return response.data;
};

export const createVideo = async (data: FormData) => {
  const response = await api.post('/api/admin/videos', data);
  return response.data;
};

export const updateVideo = async (id: string, data: FormData) => {
  const response = await api.put(`/api/admin/videos/${id}`, data);
  return response.data;
};

export const deleteVideo = async (id: string) => {
  const response = await api.delete(`/api/admin/videos/${id}`);
  return response.data;
};

// Files
export const getFiles = async (subjectId?: string, topicId?: string) => {
  const params = new URLSearchParams();
  if (subjectId) params.append('subject_id', subjectId);
  if (topicId) params.append('topic_id', topicId);
  const response = await api.get(`/api/files?${params.toString()}`);
  return response.data;
};

export const createFile = async (data: FormData, onProgress?: (progress: number) => void) => {
  const response = await api.post('/api/admin/files', data, {
    headers: { 'Content-Type': 'multipart/form-data' },
    onUploadProgress: (progressEvent) => {
      if (onProgress && progressEvent.total) {
        const percentCompleted = Math.round((progressEvent.loaded * 100) / progressEvent.total);
        onProgress(percentCompleted);
      }
    },
  });
  return response.data;
};

export const updateFile = async (id: string, data: FormData, onProgress?: (progress: number) => void) => {
  const response = await api.put(`/api/admin/files/${id}`, data, {
    headers: { 'Content-Type': 'multipart/form-data' },
    onUploadProgress: (progressEvent) => {
      if (onProgress && progressEvent.total) {
        const percentCompleted = Math.round((progressEvent.loaded * 100) / progressEvent.total);
        onProgress(percentCompleted);
      }
    },
  });
  return response.data;
};

export const deleteFile = async (id: string) => {
  const response = await api.delete(`/api/admin/files/${id}`);
  return response.data;
};

// Quizzes
export const getQuizzes = async (subjectId?: string, topicId?: string) => {
  const params = new URLSearchParams();
  if (subjectId) params.append('subject_id', subjectId);
  if (topicId) params.append('topic_id', topicId);
  const response = await api.get(`/api/quizzes?${params.toString()}`);
  return response.data;
};

export const createQuiz = async (data: FormData) => {
  const response = await api.post('/api/admin/quizzes', data);
  return response.data;
};

export const updateQuiz = async (id: string, data: FormData) => {
  const response = await api.put(`/api/admin/quizzes/${id}`, data);
  return response.data;
};

export const deleteQuiz = async (id: string) => {
  const response = await api.delete(`/api/admin/quizzes/${id}`);
  return response.data;
};

// Tips
export const getTips = async (subjectId?: string, topicId?: string) => {
  const params = new URLSearchParams();
  if (subjectId) params.append('subject_id', subjectId);
  if (topicId) params.append('topic_id', topicId);
  const response = await api.get(`/api/tips?${params.toString()}`);
  return response.data;
};

export const createTip = async (data: FormData) => {
  const response = await api.post('/api/admin/tips', data);
  return response.data;
};

export const updateTip = async (id: string, data: FormData) => {
  const response = await api.put(`/api/admin/tips/${id}`, data);
  return response.data;
};

export const deleteTip = async (id: string) => {
  const response = await api.delete(`/api/admin/tips/${id}`);
  return response.data;
};

// AI
export const chatWithAI = async (messages: Array<{ role: string; content: string }>) => {
  const response = await api.post('/api/ai/chat', { messages });
  return response.data;
};

export const getAISuggestions = async () => {
  const response = await api.get('/api/ai/suggestions');
  return response.data;
};

export default api;
