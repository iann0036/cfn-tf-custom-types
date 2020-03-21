# Terraform::CloudStack::Template

Registers an existing template into the CloudStack cloud.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::CloudStack::Template",
    "Properties" : {
        "<a href="#displaytext" title="DisplayText">DisplayText</a>" : <i>String</i>,
        "<a href="#format" title="Format">Format</a>" : <i>String</i>,
        "<a href="#hypervisor" title="Hypervisor">Hypervisor</a>" : <i>String</i>,
        "<a href="#isdynamicallyscalable" title="IsDynamicallyScalable">IsDynamicallyScalable</a>" : <i>Boolean</i>,
        "<a href="#isextractable" title="IsExtractable">IsExtractable</a>" : <i>Boolean</i>,
        "<a href="#isfeatured" title="IsFeatured">IsFeatured</a>" : <i>Boolean</i>,
        "<a href="#ispublic" title="IsPublic">IsPublic</a>" : <i>Boolean</i>,
        "<a href="#isreadytimeout" title="IsReadyTimeout">IsReadyTimeout</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#ostype" title="OsType">OsType</a>" : <i>String</i>,
        "<a href="#passwordenabled" title="PasswordEnabled">PasswordEnabled</a>" : <i>Boolean</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#url" title="Url">Url</a>" : <i>String</i>,
        "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::CloudStack::Template
Properties:
    <a href="#displaytext" title="DisplayText">DisplayText</a>: <i>String</i>
    <a href="#format" title="Format">Format</a>: <i>String</i>
    <a href="#hypervisor" title="Hypervisor">Hypervisor</a>: <i>String</i>
    <a href="#isdynamicallyscalable" title="IsDynamicallyScalable">IsDynamicallyScalable</a>: <i>Boolean</i>
    <a href="#isextractable" title="IsExtractable">IsExtractable</a>: <i>Boolean</i>
    <a href="#isfeatured" title="IsFeatured">IsFeatured</a>: <i>Boolean</i>
    <a href="#ispublic" title="IsPublic">IsPublic</a>: <i>Boolean</i>
    <a href="#isreadytimeout" title="IsReadyTimeout">IsReadyTimeout</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#ostype" title="OsType">OsType</a>: <i>String</i>
    <a href="#passwordenabled" title="PasswordEnabled">PasswordEnabled</a>: <i>Boolean</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#url" title="Url">Url</a>: <i>String</i>
    <a href="#zone" title="Zone">Zone</a>: <i>String</i>
</pre>

## Properties

#### DisplayText

The display name of the template.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Format

The format of the template. Valid values are `QCOW2`,
`RAW`, and `VHD`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hypervisor

The target hypervisor for the template. Changing
this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsDynamicallyScalable

Set to indicate if the template contains
tools to support dynamic scaling of VM cpu/memory (defaults false).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsExtractable

Set to indicate if the template is extractable
(defaults false).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsFeatured

Set to indicate if the template is featured
(defaults false).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsPublic

Set to indicate if the template is available for
all accounts (defaults true).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsReadyTimeout

The maximum time in seconds to wait until the
template is ready for use (defaults 300 seconds).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the template.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsType

The OS Type that best represents the OS of this
template.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordEnabled

Set to indicate if the template should be
password enabled (defaults false).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The name or ID of the project to create this template for.
Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

The URL of where the template is hosted. Changing this
forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zone

The name or ID of the zone where this template will be created.
Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### IsReady

Returns the <code>IsReady</code> value.

