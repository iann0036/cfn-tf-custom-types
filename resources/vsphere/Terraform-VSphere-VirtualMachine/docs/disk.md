# Terraform::VSphere::VirtualMachine Disk

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#attach" title="Attach">Attach</a>" : <i>Boolean</i>,
    "<a href="#datastoreid" title="DatastoreId">DatastoreId</a>" : <i>String</i>,
    "<a href="#diskmode" title="DiskMode">DiskMode</a>" : <i>String</i>,
    "<a href="#disksharing" title="DiskSharing">DiskSharing</a>" : <i>String</i>,
    "<a href="#eagerlyscrub" title="EagerlyScrub">EagerlyScrub</a>" : <i>Boolean</i>,
    "<a href="#iolimit" title="IoLimit">IoLimit</a>" : <i>Double</i>,
    "<a href="#ioreservation" title="IoReservation">IoReservation</a>" : <i>Double</i>,
    "<a href="#iosharecount" title="IoShareCount">IoShareCount</a>" : <i>Double</i>,
    "<a href="#iosharelevel" title="IoShareLevel">IoShareLevel</a>" : <i>String</i>,
    "<a href="#keeponremove" title="KeepOnRemove">KeepOnRemove</a>" : <i>Boolean</i>,
    "<a href="#label" title="Label">Label</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#path" title="Path">Path</a>" : <i>String</i>,
    "<a href="#size" title="Size">Size</a>" : <i>Double</i>,
    "<a href="#storagepolicyid" title="StoragePolicyId">StoragePolicyId</a>" : <i>String</i>,
    "<a href="#thinprovisioned" title="ThinProvisioned">ThinProvisioned</a>" : <i>Boolean</i>,
    "<a href="#unitnumber" title="UnitNumber">UnitNumber</a>" : <i>Double</i>,
    "<a href="#writethrough" title="WriteThrough">WriteThrough</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#attach" title="Attach">Attach</a>: <i>Boolean</i>
<a href="#datastoreid" title="DatastoreId">DatastoreId</a>: <i>String</i>
<a href="#diskmode" title="DiskMode">DiskMode</a>: <i>String</i>
<a href="#disksharing" title="DiskSharing">DiskSharing</a>: <i>String</i>
<a href="#eagerlyscrub" title="EagerlyScrub">EagerlyScrub</a>: <i>Boolean</i>
<a href="#iolimit" title="IoLimit">IoLimit</a>: <i>Double</i>
<a href="#ioreservation" title="IoReservation">IoReservation</a>: <i>Double</i>
<a href="#iosharecount" title="IoShareCount">IoShareCount</a>: <i>Double</i>
<a href="#iosharelevel" title="IoShareLevel">IoShareLevel</a>: <i>String</i>
<a href="#keeponremove" title="KeepOnRemove">KeepOnRemove</a>: <i>Boolean</i>
<a href="#label" title="Label">Label</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#path" title="Path">Path</a>: <i>String</i>
<a href="#size" title="Size">Size</a>: <i>Double</i>
<a href="#storagepolicyid" title="StoragePolicyId">StoragePolicyId</a>: <i>String</i>
<a href="#thinprovisioned" title="ThinProvisioned">ThinProvisioned</a>: <i>Boolean</i>
<a href="#unitnumber" title="UnitNumber">UnitNumber</a>: <i>Double</i>
<a href="#writethrough" title="WriteThrough">WriteThrough</a>: <i>Boolean</i>
</pre>

## Properties

#### Attach

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatastoreId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskSharing

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EagerlyScrub

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IoLimit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IoReservation

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IoShareCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IoShareLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeepOnRemove

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Label

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StoragePolicyId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThinProvisioned

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnitNumber

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WriteThrough

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

