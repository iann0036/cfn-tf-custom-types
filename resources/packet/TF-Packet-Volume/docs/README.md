# TF::Packet::Volume

Provides an Equinix Metal Block Storage Volume resource to allow you to
manage block volumes on your account.
Once created by Terraform, they must then be attached and mounted
using the api and `packet_block_attach` and `packet_block_detach`
scripts.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Packet::Volume",
    "Properties" : {
        "<a href="#billingcycle" title="BillingCycle">BillingCycle</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#facility" title="Facility">Facility</a>" : <i>String</i>,
        "<a href="#locked" title="Locked">Locked</a>" : <i>Boolean</i>,
        "<a href="#plan" title="Plan">Plan</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#size" title="Size">Size</a>" : <i>Double</i>,
        "<a href="#snapshotpolicies" title="SnapshotPolicies">SnapshotPolicies</a>" : <i>[ <a href="snapshotpoliciesdefinition.md">SnapshotPoliciesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Packet::Volume
Properties:
    <a href="#billingcycle" title="BillingCycle">BillingCycle</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#facility" title="Facility">Facility</a>: <i>String</i>
    <a href="#locked" title="Locked">Locked</a>: <i>Boolean</i>
    <a href="#plan" title="Plan">Plan</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#size" title="Size">Size</a>: <i>Double</i>
    <a href="#snapshotpolicies" title="SnapshotPolicies">SnapshotPolicies</a>: <i>
      - <a href="snapshotpoliciesdefinition.md">SnapshotPoliciesDefinition</a></i>
</pre>

## Properties

#### BillingCycle

The billing cycle, defaults to "hourly".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Optional description for the volume.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Facility

The facility to create the volume in.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Locked

Lock or unlock the volume.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Plan

The service plan slug of the volume.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

The packet project ID to deploy the volume in.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

The size in GB to make the volume.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotPolicies

_Required_: No

_Type_: List of <a href="snapshotpoliciesdefinition.md">SnapshotPoliciesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Attachments

Returns the <code>Attachments</code> value.

#### Created

Returns the <code>Created</code> value.

#### Id

Returns the <code>Id</code> value.

#### Name

Returns the <code>Name</code> value.

#### State

Returns the <code>State</code> value.

#### Updated

Returns the <code>Updated</code> value.

