import React, { useState, useEffect } from 'react';
import { StyleSheet, Text, View, FlatList, ActivityIndicator, SafeAreaView } from 'react-native';

export default function App() {
  const [horses, setHorses] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchHorses();
  }, []);

  const fetchHorses = async () => {
    try {
      // آدرس API بک‌اند که در ترموکس اجرا شده است
      const response = await fetch('http://127.0.0.1:8000/api/horses');
      const data = await response.json();
      setHorses(data);
    } catch (error) {
      console.error('Error fetching horses:', error);
    } finally {
      setLoading(false);
    }
  };

  const renderItem = ({ item }) => (
    <View style={styles.card}>
      <View style={styles.cardHeader}>
        <Text style={styles.title}>{item.title}</Text>
        <Text style={styles.price}>{item.price} میلیون تومان</Text>
      </View>
      <View style={styles.details}>
        <Text style={styles.detailText}>🐎 نژاد: {item.breed || 'نامشخص'}</Text>
        <Text style={styles.detailText}>📍 {item.province || 'نامشخص'} - {item.city || 'نامشخص'}</Text>
        <Text style={styles.detailText}>🎂 سن: {item.age ? `${item.age} سال` : 'نامشخص'}</Text>
      </View>
    </View>
  );

  if (loading) {
    return (
      <View style={styles.center}>
        <ActivityIndicator size="large" color="#10B981" />
        <Text style={styles.loadingText}>در حال دریافت آگهی‌ها...</Text>
      </View>
    );
  }

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.headerTitle}>🐎 اسب ایران</Text>
        <Text style={styles.headerSubtitle}>بازار آنلاین خرید و فروش اسب</Text>
      </View>
      <FlatList
        data={horses}
        keyExtractor={(item) => item.id.toString()}
        renderItem={renderItem}
        contentContainerStyle={styles.list}
      />
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F3F4F6',
  },
  header: {
    padding: 20,
    backgroundColor: '#FFFFFF',
    borderBottomWidth: 1,
    borderBottomColor: '#E5E7EB',
    alignItems: 'center',
  },
  headerTitle: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#059669', // سبز حرفه‌ای
  },
  headerSubtitle: {
    fontSize: 14,
    color: '#6B7280',
    marginTop: 4,
  },
  list: {
    padding: 16,
  },
  card: {
    backgroundColor: '#FFFFFF',
    borderRadius: 16,
    padding: 16,
    marginBottom: 16,
    // افکت سایه مینیمال و حرفه‌ای
    shadowColor: '#10B981',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.1,
    shadowRadius: 8,
    elevation: 4,
    borderLeftWidth: 4,
    borderLeftColor: '#F97316', // خط نارنجی برای تاکید و زیبایی
  },
  cardHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 12,
  },
  title: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#1F2937',
    flex: 1,
  },
  price: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#F97316', // نارنجی برای قیمت
  },
  details: {
    gap: 6,
  },
  detailText: {
    fontSize: 14,
    color: '#4B5563',
  },
  center: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  loadingText: {
    marginTop: 12,
    color: '#059669',
    fontSize: 16,
  },
});
