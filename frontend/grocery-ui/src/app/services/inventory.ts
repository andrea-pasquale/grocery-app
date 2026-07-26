import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';


export interface Product {
  id: number;
  name: string;
  category: string | null;
}


export interface InventoryItem {
  id: number;
  product: Product;
  quantity: number;
  unit: string;
  location: string;
  expiration_date: string | null;
  notes: string | null;
}


@Injectable({
  providedIn: 'root'
})
export class InventoryService {
  private http = inject(HttpClient);

  private apiUrl = 'http://localhost:8000/inventory/';

  getInventory() {
    return this.http.get<InventoryItem[]>(this.apiUrl);
  }
}
