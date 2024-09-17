// DO NOT EDIT! This file was auto-generated by crates/build/re_types_builder/src/codegen/cpp/mod.rs
// Based on "crates/store/re_types/definitions/rerun/components/range1d.fbs".

#pragma once

#include "../datatypes/range1d.hpp"
#include "../result.hpp"

#include <array>
#include <cstdint>
#include <memory>

namespace rerun::components {
    /// **Component**: A 1D range, specifying a lower and upper bound.
    struct Range1D {
        rerun::datatypes::Range1D range;

      public:
        Range1D() = default;

        Range1D(rerun::datatypes::Range1D range_) : range(range_) {}

        Range1D& operator=(rerun::datatypes::Range1D range_) {
            range = range_;
            return *this;
        }

        Range1D(std::array<double, 2> range_) : range(range_) {}

        Range1D& operator=(std::array<double, 2> range_) {
            range = range_;
            return *this;
        }

        /// Cast to the underlying Range1D datatype
        operator rerun::datatypes::Range1D() const {
            return range;
        }
    };
} // namespace rerun::components

namespace rerun {
    static_assert(sizeof(rerun::datatypes::Range1D) == sizeof(components::Range1D));

    /// \private
    template <>
    struct Loggable<components::Range1D> {
        static constexpr const char Name[] = "rerun.components.Range1D";

        /// Returns the arrow data type this type corresponds to.
        static const std::shared_ptr<arrow::DataType>& arrow_datatype() {
            return Loggable<rerun::datatypes::Range1D>::arrow_datatype();
        }

        /// Serializes an array of `rerun::components::Range1D` into an arrow array.
        static Result<std::shared_ptr<arrow::Array>> to_arrow(
            const components::Range1D* instances, size_t num_instances
        ) {
            if (num_instances == 0) {
                return Loggable<rerun::datatypes::Range1D>::to_arrow(nullptr, 0);
            } else if (instances == nullptr) {
                return rerun::Error(
                    ErrorCode::UnexpectedNullArgument,
                    "Passed array instances is null when num_elements> 0."
                );
            } else {
                return Loggable<rerun::datatypes::Range1D>::to_arrow(
                    &instances->range,
                    num_instances
                );
            }
        }
    };
} // namespace rerun
