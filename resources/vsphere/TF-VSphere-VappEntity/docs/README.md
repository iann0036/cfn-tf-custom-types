# TF::VSphere::VappEntity

The `vsphere_vapp_entity` resource can be used to describe the behavior of an
entity (virtual machine or sub-vApp container) in a vApp container.

For more information on vSphere vApps, see [this
page][ref-vsphere-vapp].

[ref-vsphere-vapp]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vm_admin.doc/GUID-2A95EBB8-1779-40FA-B4FB-4D0845750879.html

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::VSphere::VappEntity",
    "Properties" : {
        "<a href="#containerid" title="ContainerId">ContainerId</a>" : <i>String</i>,
        "<a href="#customattributes" title="CustomAttributes">CustomAttributes</a>" : <i>[ <a href="customattributesdefinition.md">CustomAttributesDefinition</a>, ... ]</i>,
        "<a href="#startaction" title="StartAction">StartAction</a>" : <i>String</i>,
        "<a href="#startdelay" title="StartDelay">StartDelay</a>" : <i>Double</i>,
        "<a href="#startorder" title="StartOrder">StartOrder</a>" : <i>Double</i>,
        "<a href="#stopaction" title="StopAction">StopAction</a>" : <i>String</i>,
        "<a href="#stopdelay" title="StopDelay">StopDelay</a>" : <i>Double</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#targetid" title="TargetId">TargetId</a>" : <i>String</i>,
        "<a href="#waitforguest" title="WaitForGuest">WaitForGuest</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::VSphere::VappEntity
Properties:
    <a href="#containerid" title="ContainerId">ContainerId</a>: <i>String</i>
    <a href="#customattributes" title="CustomAttributes">CustomAttributes</a>: <i>
      - <a href="customattributesdefinition.md">CustomAttributesDefinition</a></i>
    <a href="#startaction" title="StartAction">StartAction</a>: <i>String</i>
    <a href="#startdelay" title="StartDelay">StartDelay</a>: <i>Double</i>
    <a href="#startorder" title="StartOrder">StartOrder</a>: <i>Double</i>
    <a href="#stopaction" title="StopAction">StopAction</a>: <i>String</i>
    <a href="#stopdelay" title="StopDelay">StopDelay</a>: <i>Double</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#targetid" title="TargetId">TargetId</a>: <i>String</i>
    <a href="#waitforguest" title="WaitForGuest">WaitForGuest</a>: <i>Boolean</i>
</pre>

## Properties

#### ContainerId

[Managed object ID|docs-about-morefs] of the vApp
container the entity is a member of.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomAttributes

_Required_: No

_Type_: List of <a href="customattributesdefinition.md">CustomAttributesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartAction

How to start the entity. Valid settings are none
or powerOn. If set to none, then the entity does not participate in auto-start.
Default: powerOn.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartDelay

Delay in seconds before continuing with the next
entity in the order of entities to be started. Default: 120.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartOrder

Order to start and stop target in vApp. Default: 1.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StopAction

Defines the stop action for the entity. Can be set
to none, powerOff, guestShutdown, or suspend. If set to none, then the entity
does not participate in auto-stop. Default: powerOff.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StopDelay

Delay in seconds before continuing with the next
entity in the order sequence. This is only used if the stopAction is
guestShutdown. Default: 120.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetId

[Managed object ID|docs-about-morefs] of the entity
to power on or power off. This can be a virtual machine or a vApp.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitForGuest

Determines if the VM should be marked as being
started when VMware Tools are ready instead of waiting for `start_delay`. This
property has no effect for vApps. Default: false.

_Required_: No

_Type_: Boolean

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

