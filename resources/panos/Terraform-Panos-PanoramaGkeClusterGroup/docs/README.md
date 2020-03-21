# Terraform::Panos::PanoramaGkeClusterGroup

This resource allows you to add/update/delete a GKE cluster group.

This resource requires that the GCP plugin be installed.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::PanoramaGkeClusterGroup",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#devicegroup" title="DeviceGroup">DeviceGroup</a>" : <i>String</i>,
        "<a href="#gcpprojectcredential" title="GcpProjectCredential">GcpProjectCredential</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#templatestack" title="TemplateStack">TemplateStack</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::PanoramaGkeClusterGroup
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#devicegroup" title="DeviceGroup">DeviceGroup</a>: <i>String</i>
    <a href="#gcpprojectcredential" title="GcpProjectCredential">GcpProjectCredential</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#templatestack" title="TemplateStack">TemplateStack</a>: <i>String</i>
</pre>

## Properties

#### Description

The description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceGroup

The device group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcpProjectCredential

The GCP account to use.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The cluster group's name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateStack

The template stack.

_Required_: Yes

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

