# Terraform::AWS::SpotFleetRequest LaunchSpecification

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ami" title="Ami">Ami</a>" : <i>String</i>,
    "<a href="#associatepublicipaddress" title="AssociatePublicIpAddress">AssociatePublicIpAddress</a>" : <i>Boolean</i>,
    "<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>" : <i>String</i>,
    "<a href="#ebsoptimized" title="EbsOptimized">EbsOptimized</a>" : <i>Boolean</i>,
    "<a href="#iaminstanceprofile" title="IamInstanceProfile">IamInstanceProfile</a>" : <i>String</i>,
    "<a href="#iaminstanceprofilearn" title="IamInstanceProfileArn">IamInstanceProfileArn</a>" : <i>String</i>,
    "<a href="#instancetype" title="InstanceType">InstanceType</a>" : <i>String</i>,
    "<a href="#keyname" title="KeyName">KeyName</a>" : <i>String</i>,
    "<a href="#monitoring" title="Monitoring">Monitoring</a>" : <i>Boolean</i>,
    "<a href="#placementgroup" title="PlacementGroup">PlacementGroup</a>" : <i>String</i>,
    "<a href="#placementtenancy" title="PlacementTenancy">PlacementTenancy</a>" : <i>String</i>,
    "<a href="#spotprice" title="SpotPrice">SpotPrice</a>" : <i>String</i>,
    "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
    "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;launchspecification-tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
    "<a href="#userdata" title="UserData">UserData</a>" : <i>String</i>,
    "<a href="#vpcsecuritygroupids" title="VpcSecurityGroupIds">VpcSecurityGroupIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#weightedcapacity" title="WeightedCapacity">WeightedCapacity</a>" : <i>String</i>,
    "<a href="#ebsblockdevice" title="EbsBlockDevice">EbsBlockDevice</a>" : <i>[ &lt;a href=&#34;launchspecification-ebsblockdevice.md&#34;&gt;EbsBlockDevice&lt;/a&gt;, ... ]</i>,
    "<a href="#ephemeralblockdevice" title="EphemeralBlockDevice">EphemeralBlockDevice</a>" : <i>[ &lt;a href=&#34;launchspecification-ephemeralblockdevice.md&#34;&gt;EphemeralBlockDevice&lt;/a&gt;, ... ]</i>,
    "<a href="#rootblockdevice" title="RootBlockDevice">RootBlockDevice</a>" : <i>[ &lt;a href=&#34;launchspecification-rootblockdevice.md&#34;&gt;RootBlockDevice&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ami" title="Ami">Ami</a>: <i>String</i>
<a href="#associatepublicipaddress" title="AssociatePublicIpAddress">AssociatePublicIpAddress</a>: <i>Boolean</i>
<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>: <i>String</i>
<a href="#ebsoptimized" title="EbsOptimized">EbsOptimized</a>: <i>Boolean</i>
<a href="#iaminstanceprofile" title="IamInstanceProfile">IamInstanceProfile</a>: <i>String</i>
<a href="#iaminstanceprofilearn" title="IamInstanceProfileArn">IamInstanceProfileArn</a>: <i>String</i>
<a href="#instancetype" title="InstanceType">InstanceType</a>: <i>String</i>
<a href="#keyname" title="KeyName">KeyName</a>: <i>String</i>
<a href="#monitoring" title="Monitoring">Monitoring</a>: <i>Boolean</i>
<a href="#placementgroup" title="PlacementGroup">PlacementGroup</a>: <i>String</i>
<a href="#placementtenancy" title="PlacementTenancy">PlacementTenancy</a>: <i>String</i>
<a href="#spotprice" title="SpotPrice">SpotPrice</a>: <i>String</i>
<a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
<a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;launchspecification-tags.md&#34;&gt;Tags&lt;/a&gt;</i>
<a href="#userdata" title="UserData">UserData</a>: <i>String</i>
<a href="#vpcsecuritygroupids" title="VpcSecurityGroupIds">VpcSecurityGroupIds</a>: <i>
      - String</i>
<a href="#weightedcapacity" title="WeightedCapacity">WeightedCapacity</a>: <i>String</i>
<a href="#ebsblockdevice" title="EbsBlockDevice">EbsBlockDevice</a>: <i>
      - &lt;a href=&#34;launchspecification-ebsblockdevice.md&#34;&gt;EbsBlockDevice&lt;/a&gt;</i>
<a href="#ephemeralblockdevice" title="EphemeralBlockDevice">EphemeralBlockDevice</a>: <i>
      - &lt;a href=&#34;launchspecification-ephemeralblockdevice.md&#34;&gt;EphemeralBlockDevice&lt;/a&gt;</i>
<a href="#rootblockdevice" title="RootBlockDevice">RootBlockDevice</a>: <i>
      - &lt;a href=&#34;launchspecification-rootblockdevice.md&#34;&gt;RootBlockDevice&lt;/a&gt;</i>
</pre>

## Properties

#### Ami

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssociatePublicIpAddress

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilityZone

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EbsOptimized

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IamInstanceProfile

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IamInstanceProfileArn

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceType

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyName

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Monitoring

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlacementGroup

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlacementTenancy

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpotPrice

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No
_Type_: List of &lt;a href=&#34;launchspecification-tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserData

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcSecurityGroupIds

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WeightedCapacity

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EbsBlockDevice

_Required_: No
_Type_: List of &lt;a href=&#34;launchspecification-ebsblockdevice.md&#34;&gt;EbsBlockDevice&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EphemeralBlockDevice

_Required_: No
_Type_: List of &lt;a href=&#34;launchspecification-ephemeralblockdevice.md&#34;&gt;EphemeralBlockDevice&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RootBlockDevice

_Required_: No
_Type_: List of &lt;a href=&#34;launchspecification-rootblockdevice.md&#34;&gt;RootBlockDevice&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

