# Terraform::HCloud::FloatingIp

Provides a Hetzner Cloud Floating IP to represent a publicly-accessible static IP address that can be mapped to one of your servers.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::HCloud::FloatingIp",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#homelocation" title="HomeLocation">HomeLocation</a>" : <i>String</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labels.md">Labels</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#serverid" title="ServerId">ServerId</a>" : <i>Double</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::HCloud::FloatingIp
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#homelocation" title="HomeLocation">HomeLocation</a>: <i>String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labels.md">Labels</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#serverid" title="ServerId">ServerId</a>: <i>Double</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### Description

Description of the Floating IP.
- `labels` - (Optional, map) User-defined labels (key-value pairs) should be created with.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HomeLocation

Home location (routing is optimized for that location). Optional if server_id argument is passed.
- `description` - (Optional, string) Description of the Floating IP.
- `labels` - (Optional, map) User-defined labels (key-value pairs) should be created with.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

User-defined labels (key-value pairs) should be created with.

_Required_: No

_Type_: List of <a href="labels.md">Labels</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the Floating IP.
- `server_id` - (Optional, int) Server to assign the Floating IP to.
- `home_location` - (Optional, string) Home location (routing is optimized for that location). Optional if server_id argument is passed.
- `description` - (Optional, string) Description of the Floating IP.
- `labels` - (Optional, map) User-defined labels (key-value pairs) should be created with.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerId

Server to assign the Floating IP to.
- `home_location` - (Optional, string) Home location (routing is optimized for that location). Optional if server_id argument is passed.
- `description` - (Optional, string) Description of the Floating IP.
- `labels` - (Optional, map) User-defined labels (key-value pairs) should be created with.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Type of the Floating IP. `ipv4` `ipv6`
- `name` - (Optional, string) Name of the Floating IP.
- `server_id` - (Optional, int) Server to assign the Floating IP to.
- `home_location` - (Optional, string) Home location (routing is optimized for that location). Optional if server_id argument is passed.
- `description` - (Optional, string) Description of the Floating IP.
- `labels` - (Optional, map) User-defined labels (key-value pairs) should be created with.

_Required_: Yes

_Type_: String

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

#### IpAddress

Returns the <code>IpAddress</code> value.

#### IpNetwork

Returns the <code>IpNetwork</code> value.

