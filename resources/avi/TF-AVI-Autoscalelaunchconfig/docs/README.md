# TF::AVI::Autoscalelaunchconfig

The AutoScaleLaunchConfig resource allows the creation and management of Avi AutoScaleLaunchConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Autoscalelaunchconfig",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#imageid" title="ImageId">ImageId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#tenantref" title="TenantRef">TenantRef</a>" : <i>String</i>,
        "<a href="#useexternalasg" title="UseExternalAsg">UseExternalAsg</a>" : <i>Boolean</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#markers" title="Markers">Markers</a>" : <i>[ <a href="markersdefinition.md">MarkersDefinition</a>, ... ]</i>,
        "<a href="#mesos" title="Mesos">Mesos</a>" : <i>[ <a href="mesosdefinition.md">MesosDefinition</a>, ... ]</i>,
        "<a href="#openstack" title="Openstack">Openstack</a>" : <i>[ <a href="openstackdefinition.md">OpenstackDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Autoscalelaunchconfig
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#imageid" title="ImageId">ImageId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#tenantref" title="TenantRef">TenantRef</a>: <i>String</i>
    <a href="#useexternalasg" title="UseExternalAsg">UseExternalAsg</a>: <i>Boolean</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#markers" title="Markers">Markers</a>: <i>
      - <a href="markersdefinition.md">MarkersDefinition</a></i>
    <a href="#mesos" title="Mesos">Mesos</a>: <i>
      - <a href="mesosdefinition.md">MesosDefinition</a></i>
    <a href="#openstack" title="Openstack">Openstack</a>: <i>
      - <a href="openstackdefinition.md">OpenstackDefinition</a></i>
</pre>

## Properties

#### Description

User defined description for the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageId

Unique id of the amazon machine image (ami)  or openstack vm id.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the object.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantRef

It is a reference to an object of type tenant.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseExternalAsg

If set to true, serverautoscalepolicy will use the autoscaling group (external_autoscaling_groups) from pool to perform scale up and scale down. Pool should have single autoscaling group configured. Field introduced in 17.2.3.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Markers

_Required_: No

_Type_: List of <a href="markersdefinition.md">MarkersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mesos

_Required_: No

_Type_: List of <a href="mesosdefinition.md">MesosDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Openstack

_Required_: No

_Type_: List of <a href="openstackdefinition.md">OpenstackDefinition</a>

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

