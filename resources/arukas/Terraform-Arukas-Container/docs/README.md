# Terraform::Arukas::Container

Provides container resource. This allows container to be created, updated and deleted.

For additional details please refer to [API documentation](https://arukas.io/en/documents-en/arukas-api-reference-en/).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Arukas::Container",
    "Properties" : {
        "<a href="#cmd" title="Cmd">Cmd</a>" : <i>String</i>,
        "<a href="#endpoint" title="Endpoint">Endpoint</a>" : <i>String</i>,
        "<a href="#image" title="Image">Image</a>" : <i>String</i>,
        "<a href="#instances" title="Instances">Instances</a>" : <i>Double</i>,
        "<a href="#memory" title="Memory">Memory</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#plan" title="Plan">Plan</a>" : <i>String</i>,
        "<a href="#environments" title="Environments">Environments</a>" : <i>[ <a href="environments.md">Environments</a>, ... ]</i>,
        "<a href="#ports" title="Ports">Ports</a>" : <i>[ <a href="ports.md">Ports</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Arukas::Container
Properties:
    <a href="#cmd" title="Cmd">Cmd</a>: <i>String</i>
    <a href="#endpoint" title="Endpoint">Endpoint</a>: <i>String</i>
    <a href="#image" title="Image">Image</a>: <i>String</i>
    <a href="#instances" title="Instances">Instances</a>: <i>Double</i>
    <a href="#memory" title="Memory">Memory</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#plan" title="Plan">Plan</a>: <i>String</i>
    <a href="#environments" title="Environments">Environments</a>: <i>
      - <a href="environments.md">Environments</a></i>
    <a href="#ports" title="Ports">Ports</a>: <i>
      - <a href="ports.md">Ports</a></i>
</pre>

## Properties

#### Cmd

The command of the container.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Endpoint

The subdomain part of the endpoint assigned by Arukas. If it is not set, Arukas will do automatic assignment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Image

The ID of the image to back this container.It must be a public image on DockerHub.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Instances

The count of the instance. It must be between `1` and `10`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Memory

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the container.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Plan

The plan of the Arukas. It must be `free` or `hobby` or `standard-1` or `standard-2`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Environments

_Required_: No

_Type_: List of <a href="environments.md">Environments</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ports

_Required_: No

_Type_: List of <a href="ports.md">Ports</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### EndpointFullHostname

Returns the <code>EndpointFullHostname</code> value.

#### EndpointFullUrl

Returns the <code>EndpointFullUrl</code> value.

#### Id

Returns the <code>Id</code> value.

#### PortMappings

Returns the <code>PortMappings</code> value.

#### Region

Returns the <code>Region</code> value.

#### ServiceId

Returns the <code>ServiceId</code> value.

