import { Component, inject, signal } from '@angular/core';
import { InventoryService, InventoryItem } from '../../services/inventory';

@Component({
  selector: 'app-inventory',
  imports: [],
  templateUrl: './inventory.html',
  styleUrl: './inventory.css'
})
export class Inventory {

  private inventoryService = inject(InventoryService);

  items = signal<InventoryItem[]>([]);

  ngOnInit() {
    this.inventoryService.getInventory()
      .subscribe(data => {
        this.items.set(data);
      });
  }
}
