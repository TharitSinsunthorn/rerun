// DO NOT EDIT! This file was auto-generated by crates/build/re_types_builder/src/codegen/rust/api.rs
// Based on "crates/store/re_types/definitions/rerun/components/transform_mat3x3.fbs".

#![allow(unused_imports)]
#![allow(unused_parens)]
#![allow(clippy::clone_on_copy)]
#![allow(clippy::cloned_instead_of_copied)]
#![allow(clippy::map_flatten)]
#![allow(clippy::needless_question_mark)]
#![allow(clippy::new_without_default)]
#![allow(clippy::redundant_closure)]
#![allow(clippy::too_many_arguments)]
#![allow(clippy::too_many_lines)]

use ::re_types_core::external::arrow2;
use ::re_types_core::ComponentName;
use ::re_types_core::SerializationResult;
use ::re_types_core::{ComponentBatch, MaybeOwnedComponentBatch};
use ::re_types_core::{DeserializationError, DeserializationResult};

/// **Component**: A 3x3 transformation matrix Matrix that doesn't propagate in the transform hierarchy.
///
/// 3x3 matrixes are able to represent any affine transformation in 3D space,
/// i.e. rotation, scaling, shearing, reflection etc.
///
/// Matrices in Rerun are stored as flat list of coefficients in column-major order:
/// ```text
///             column 0       column 1       column 2
///        -------------------------------------------------
/// row 0 | flat_columns[0] flat_columns[3] flat_columns[6]
/// row 1 | flat_columns[1] flat_columns[4] flat_columns[7]
/// row 2 | flat_columns[2] flat_columns[5] flat_columns[8]
/// ```
#[derive(Clone, Debug, Default, Copy, PartialEq, bytemuck::Pod, bytemuck::Zeroable)]
#[repr(transparent)]
pub struct LeafTransformMat3x3(pub crate::datatypes::Mat3x3);

impl ::re_types_core::SizeBytes for LeafTransformMat3x3 {
    #[inline]
    fn heap_size_bytes(&self) -> u64 {
        self.0.heap_size_bytes()
    }

    #[inline]
    fn is_pod() -> bool {
        <crate::datatypes::Mat3x3>::is_pod()
    }
}

impl<T: Into<crate::datatypes::Mat3x3>> From<T> for LeafTransformMat3x3 {
    fn from(v: T) -> Self {
        Self(v.into())
    }
}

impl std::borrow::Borrow<crate::datatypes::Mat3x3> for LeafTransformMat3x3 {
    #[inline]
    fn borrow(&self) -> &crate::datatypes::Mat3x3 {
        &self.0
    }
}

impl std::ops::Deref for LeafTransformMat3x3 {
    type Target = crate::datatypes::Mat3x3;

    #[inline]
    fn deref(&self) -> &crate::datatypes::Mat3x3 {
        &self.0
    }
}

impl std::ops::DerefMut for LeafTransformMat3x3 {
    #[inline]
    fn deref_mut(&mut self) -> &mut crate::datatypes::Mat3x3 {
        &mut self.0
    }
}

::re_types_core::macros::impl_into_cow!(LeafTransformMat3x3);

impl ::re_types_core::Loggable for LeafTransformMat3x3 {
    type Name = ::re_types_core::ComponentName;

    #[inline]
    fn name() -> Self::Name {
        "rerun.components.LeafTransformMat3x3".into()
    }

    #[inline]
    fn arrow_datatype() -> arrow2::datatypes::DataType {
        crate::datatypes::Mat3x3::arrow_datatype()
    }

    fn to_arrow_opt<'a>(
        data: impl IntoIterator<Item = Option<impl Into<::std::borrow::Cow<'a, Self>>>>,
    ) -> SerializationResult<Box<dyn arrow2::array::Array>>
    where
        Self: Clone + 'a,
    {
        crate::datatypes::Mat3x3::to_arrow_opt(data.into_iter().map(|datum| {
            datum.map(|datum| match datum.into() {
                ::std::borrow::Cow::Borrowed(datum) => ::std::borrow::Cow::Borrowed(&datum.0),
                ::std::borrow::Cow::Owned(datum) => ::std::borrow::Cow::Owned(datum.0),
            })
        }))
    }

    fn from_arrow_opt(
        arrow_data: &dyn arrow2::array::Array,
    ) -> DeserializationResult<Vec<Option<Self>>>
    where
        Self: Sized,
    {
        crate::datatypes::Mat3x3::from_arrow_opt(arrow_data)
            .map(|v| v.into_iter().map(|v| v.map(Self)).collect())
    }

    #[inline]
    fn from_arrow(arrow_data: &dyn arrow2::array::Array) -> DeserializationResult<Vec<Self>>
    where
        Self: Sized,
    {
        crate::datatypes::Mat3x3::from_arrow(arrow_data).map(bytemuck::cast_vec)
    }
}
