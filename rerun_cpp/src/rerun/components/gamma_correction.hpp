// DO NOT EDIT! This file was auto-generated by crates/build/re_types_builder/src/codegen/cpp/mod.rs
// Based on "crates/store/re_types/definitions/rerun/components/gamma_correction.fbs".

#pragma once

#include "../datatypes/float32.hpp"
#include "../result.hpp"

#include <cstdint>
#include <memory>

namespace rerun::components {
    /// **Component**: A gamma correction value to be used with a scalar value or color.
    ///
    /// Used to adjust the gamma of a color or scalar value between 0 and 1 before rendering.
    /// `new_value = old_value ^ gamma`
    ///
    /// Valid range is from 0 (excluding) to max float.
    /// Defaults to 1.0 unless otherwise specified.
    struct GammaCorrection {
        rerun::datatypes::Float32 gamma;

      public:
        GammaCorrection() = default;

        GammaCorrection(rerun::datatypes::Float32 gamma_) : gamma(gamma_) {}

        GammaCorrection& operator=(rerun::datatypes::Float32 gamma_) {
            gamma = gamma_;
            return *this;
        }

        GammaCorrection(float value_) : gamma(value_) {}

        GammaCorrection& operator=(float value_) {
            gamma = value_;
            return *this;
        }

        /// Cast to the underlying Float32 datatype
        operator rerun::datatypes::Float32() const {
            return gamma;
        }
    };
} // namespace rerun::components

namespace rerun {
    static_assert(sizeof(rerun::datatypes::Float32) == sizeof(components::GammaCorrection));

    /// \private
    template <>
    struct Loggable<components::GammaCorrection> {
        static constexpr const char Name[] = "rerun.components.GammaCorrection";

        /// Returns the arrow data type this type corresponds to.
        static const std::shared_ptr<arrow::DataType>& arrow_datatype() {
            return Loggable<rerun::datatypes::Float32>::arrow_datatype();
        }

        /// Serializes an array of `rerun::components::GammaCorrection` into an arrow array.
        static Result<std::shared_ptr<arrow::Array>> to_arrow(
            const components::GammaCorrection* instances, size_t num_instances
        ) {
            if (num_instances == 0) {
                return Loggable<rerun::datatypes::Float32>::to_arrow(nullptr, 0);
            } else if (instances == nullptr) {
                return rerun::Error(
                    ErrorCode::UnexpectedNullArgument,
                    "Passed array instances is null when num_elements> 0."
                );
            } else {
                return Loggable<rerun::datatypes::Float32>::to_arrow(
                    &instances->gamma,
                    num_instances
                );
            }
        }
    };
} // namespace rerun
