import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { CourseCardComponent } from '../course-card/course-card';
import { CourseService } from '../course';

@Component({
  selector: 'app-course-list',
  standalone: true,
  imports: [CommonModule, FormsModule, CourseCardComponent],
  templateUrl: './course-list.html',
  styleUrl: './course-list.css'
})
export class CourseListComponent implements OnInit {

  constructor(private courseService: CourseService) {}

  searchTerm = "";

  loading = true;

  courses: any[] = [];

  ngOnInit(): void {

    this.loading = true;

    this.courseService.getCourses().subscribe({

      next: (data: any[]) => {

        this.courses = data.map((post: any, index: number) => ({

          id: index + 1,
          name: post.title,
          code: `CS10${index + 1}`,
          credits: 3 + (index % 2),
          grade: "A"

        }));

        this.loading = false;

      },

      error: (error) => {

        console.error(error);

        this.loading = false;

      }

    });

  }

  get filteredCourses() {

    return this.courses.filter(course =>
      course.name.toLowerCase().includes(this.searchTerm.toLowerCase())
    );

  }

}