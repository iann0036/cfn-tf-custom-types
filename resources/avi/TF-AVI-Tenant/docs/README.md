# TF::AVI::Tenant

The Tenant resource allows the creation and management of Avi Tenant

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Tenant",
    "Properties" : {
        "<a href="#createdby" title="CreatedBy">CreatedBy</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enforcelabelgroup" title="EnforceLabelGroup">EnforceLabelGroup</a>" : <i>Boolean</i>,
        "<a href="#labelgrouprefs" title="LabelGroupRefs">LabelGroupRefs</a>" : <i>[ String, ... ]</i>,
        "<a href="#local" title="Local">Local</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#configsettings" title="ConfigSettings">ConfigSettings</a>" : <i>[ <a href="configsettingsdefinition.md">ConfigSettingsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Tenant
Properties:
    <a href="#createdby" title="CreatedBy">CreatedBy</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enforcelabelgroup" title="EnforceLabelGroup">EnforceLabelGroup</a>: <i>Boolean</i>
    <a href="#labelgrouprefs" title="LabelGroupRefs">LabelGroupRefs</a>: <i>
      - String</i>
    <a href="#local" title="Local">Local</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#configsettings" title="ConfigSettings">ConfigSettings</a>: <i>
      - <a href="configsettingsdefinition.md">ConfigSettingsDefinition</a></i>
</pre>

## Properties

#### CreatedBy

Creator of this tenant.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

User defined description for the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnforceLabelGroup

The referred label groups are enforced on the tenant if this is set to true.if this is set to false, the label groups are suggested for the tenant. Field introduced in 20.1.5.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LabelGroupRefs

The label_groups to be enforced on the tenant. This is strictly enforced only if enforce_label_group is set to true. It is a reference to an object of type labelgroup. Field introduced in 20.1.5.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Local

Boolean flag to set local.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the object.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigSettings

_Required_: No

_Type_: List of <a href="configsettingsdefinition.md">ConfigSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

