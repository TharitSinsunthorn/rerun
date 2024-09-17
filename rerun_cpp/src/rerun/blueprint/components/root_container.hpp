// DO NOT EDIT! This file was auto-generated by crates/build/re_types_builder/src/codegen/cpp/mod.rs
// Based on "crates/store/re_types/definitions/rerun/blueprint/components/root_container.fbs".

#pragma once

#include "../../datatypes/uuid.hpp"
#include "../../result.hpp"

#include <array>
#include <cstdint>
#include <memory>

namespace rerun::blueprint::components {
    /// **Component**: The container that sits at the root of a viewport.
    struct RootContainer {
        /// `ContainerId` for the root.
        rerun::datatypes::Uuid id;

      public:
        RootContainer() = default;

        RootContainer(rerun::datatypes::Uuid id_) : id(id_) {}

        RootContainer& operator=(rerun::datatypes::Uuid id_) {
            id = id_;
            return *this;
        }

        RootContainer(std::array<uint8_t, 16> bytes_) : id(bytes_) {}

        RootContainer& operator=(std::array<uint8_t, 16> bytes_) {
            id = bytes_;
            return *this;
        }

        /// Cast to the underlying Uuid datatype
        operator rerun::datatypes::Uuid() const {
            return id;
        }
    };
} // namespace rerun::blueprint::components

namespace rerun {
    static_assert(sizeof(rerun::datatypes::Uuid) == sizeof(blueprint::components::RootContainer));

    /// \private
    template <>
    struct Loggable<blueprint::components::RootContainer> {
        static constexpr const char Name[] = "rerun.blueprint.components.RootContainer";

        /// Returns the arrow data type this type corresponds to.
        static const std::shared_ptr<arrow::DataType>& arrow_datatype() {
            return Loggable<rerun::datatypes::Uuid>::arrow_datatype();
        }

        /// Serializes an array of `rerun::blueprint:: components::RootContainer` into an arrow array.
        static Result<std::shared_ptr<arrow::Array>> to_arrow(
            const blueprint::components::RootContainer* instances, size_t num_instances
        ) {
            if (num_instances == 0) {
                return Loggable<rerun::datatypes::Uuid>::to_arrow(nullptr, 0);
            } else if (instances == nullptr) {
                return rerun::Error(
                    ErrorCode::UnexpectedNullArgument,
                    "Passed array instances is null when num_elements> 0."
                );
            } else {
                return Loggable<rerun::datatypes::Uuid>::to_arrow(&instances->id, num_instances);
            }
        }
    };
} // namespace rerun
