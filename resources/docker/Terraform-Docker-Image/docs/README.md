# Terraform::Docker::Image

Pulls a Docker image to a given Docker host from a Docker Registry.

This resource will *not* pull new layers of the image automatically unless used in
conjunction with [`docker_registry_image`](/docs/providers/docker/d/registry_image.html)
data source to update the `pull_triggers` field.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Docker::Image",
    "Properties" : {
        "<a href="#keeplocally" title="KeepLocally">KeepLocally</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#pulltrigger" title="PullTrigger">PullTrigger</a>" : <i>String</i>,
        "<a href="#pulltriggers" title="PullTriggers">PullTriggers</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Docker::Image
Properties:
    <a href="#keeplocally" title="KeepLocally">KeepLocally</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#pulltrigger" title="PullTrigger">PullTrigger</a>: <i>String</i>
    <a href="#pulltriggers" title="PullTriggers">PullTriggers</a>: <i>
      - String</i>
</pre>

## Properties

#### KeepLocally

If true, then the Docker image won't be
deleted on destroy operation. If this is false, it will delete the image from
the docker local storage on destroy operation.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Docker image, including any tags or SHA256 repo digests.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PullTrigger

**Deprecated**, use `pull_triggers` instead.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PullTriggers

List of values which cause an
image pull when changed. This is used to store the image digest from the
registry when using the `docker_registry_image` [data source](/docs/providers/docker/d/registry_image.html)
to trigger an image update.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### Latest

Returns the <code>Latest</code> value.

