# Terraform::AWS::LaunchTemplate

CloudFormation equivalent of aws_launch_template

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::LaunchTemplate",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#arn" title="Arn">Arn</a>" : <i>String</i>,
        "<a href="#defaultversion" title="DefaultVersion">DefaultVersion</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#disableapitermination" title="DisableApiTermination">DisableApiTermination</a>" : <i>Boolean</i>,
        "<a href="#ebsoptimized" title="EbsOptimized">EbsOptimized</a>" : <i>String</i>,
        "<a href="#imageid" title="ImageId">ImageId</a>" : <i>String</i>,
        "<a href="#instanceinitiatedshutdownbehavior" title="InstanceInitiatedShutdownBehavior">InstanceInitiatedShutdownBehavior</a>" : <i>String</i>,
        "<a href="#instancetype" title="InstanceType">InstanceType</a>" : <i>String</i>,
        "<a href="#kernelid" title="KernelId">KernelId</a>" : <i>String</i>,
        "<a href="#keyname" title="KeyName">KeyName</a>" : <i>String</i>,
        "<a href="#latestversion" title="LatestVersion">LatestVersion</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nameprefix" title="NamePrefix">NamePrefix</a>" : <i>String</i>,
        "<a href="#ramdiskid" title="RamDiskId">RamDiskId</a>" : <i>String</i>,
        "<a href="#securitygroupnames" title="SecurityGroupNames">SecurityGroupNames</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#userdata" title="UserData">UserData</a>" : <i>String</i>,
        "<a href="#vpcsecuritygroupids" title="VpcSecurityGroupIds">VpcSecurityGroupIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#blockdevicemappings" title="BlockDeviceMappings">BlockDeviceMappings</a>" : <i>[ &lt;a href=&#34;blockdevicemappings.md&#34;&gt;BlockDeviceMappings&lt;/a&gt;, ... ]</i>,
        "<a href="#capacityreservationspecification" title="CapacityReservationSpecification">CapacityReservationSpecification</a>" : <i>[ &lt;a href=&#34;capacityreservationspecification.md&#34;&gt;CapacityReservationSpecification&lt;/a&gt;, ... ]</i>,
        "<a href="#cpuoptions" title="CpuOptions">CpuOptions</a>" : <i>[ &lt;a href=&#34;cpuoptions.md&#34;&gt;CpuOptions&lt;/a&gt;, ... ]</i>,
        "<a href="#creditspecification" title="CreditSpecification">CreditSpecification</a>" : <i>[ &lt;a href=&#34;creditspecification.md&#34;&gt;CreditSpecification&lt;/a&gt;, ... ]</i>,
        "<a href="#elasticgpuspecifications" title="ElasticGpuSpecifications">ElasticGpuSpecifications</a>" : <i>[ &lt;a href=&#34;elasticgpuspecifications.md&#34;&gt;ElasticGpuSpecifications&lt;/a&gt;, ... ]</i>,
        "<a href="#elasticinferenceaccelerator" title="ElasticInferenceAccelerator">ElasticInferenceAccelerator</a>" : <i>[ &lt;a href=&#34;elasticinferenceaccelerator.md&#34;&gt;ElasticInferenceAccelerator&lt;/a&gt;, ... ]</i>,
        "<a href="#iaminstanceprofile" title="IamInstanceProfile">IamInstanceProfile</a>" : <i>[ &lt;a href=&#34;iaminstanceprofile.md&#34;&gt;IamInstanceProfile&lt;/a&gt;, ... ]</i>,
        "<a href="#instancemarketoptions" title="InstanceMarketOptions">InstanceMarketOptions</a>" : <i>[ &lt;a href=&#34;instancemarketoptions.md&#34;&gt;InstanceMarketOptions&lt;/a&gt;, ... ]</i>,
        "<a href="#licensespecification" title="LicenseSpecification">LicenseSpecification</a>" : <i>[ &lt;a href=&#34;licensespecification.md&#34;&gt;LicenseSpecification&lt;/a&gt;, ... ]</i>,
        "<a href="#monitoring" title="Monitoring">Monitoring</a>" : <i>[ &lt;a href=&#34;monitoring.md&#34;&gt;Monitoring&lt;/a&gt;, ... ]</i>,
        "<a href="#networkinterfaces" title="NetworkInterfaces">NetworkInterfaces</a>" : <i>[ &lt;a href=&#34;networkinterfaces.md&#34;&gt;NetworkInterfaces&lt;/a&gt;, ... ]</i>,
        "<a href="#placement" title="Placement">Placement</a>" : <i>[ &lt;a href=&#34;placement.md&#34;&gt;Placement&lt;/a&gt;, ... ]</i>,
        "<a href="#tagspecifications" title="TagSpecifications">TagSpecifications</a>" : <i>[ &lt;a href=&#34;tagspecifications.md&#34;&gt;TagSpecifications&lt;/a&gt;, ... ]</i>,
        "<a href="#ebs" title="Ebs">Ebs</a>" : <i>[ &lt;a href=&#34;ebs.md&#34;&gt;Ebs&lt;/a&gt;, ... ]</i>,
        "<a href="#capacityreservationtarget" title="CapacityReservationTarget">CapacityReservationTarget</a>" : <i>[ &lt;a href=&#34;capacityreservationtarget.md&#34;&gt;CapacityReservationTarget&lt;/a&gt;, ... ]</i>,
        "<a href="#spotoptions" title="SpotOptions">SpotOptions</a>" : <i>[ &lt;a href=&#34;spotoptions.md&#34;&gt;SpotOptions&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::LaunchTemplate
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#arn" title="Arn">Arn</a>: <i>String</i>
    <a href="#defaultversion" title="DefaultVersion">DefaultVersion</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#disableapitermination" title="DisableApiTermination">DisableApiTermination</a>: <i>Boolean</i>
    <a href="#ebsoptimized" title="EbsOptimized">EbsOptimized</a>: <i>String</i>
    <a href="#imageid" title="ImageId">ImageId</a>: <i>String</i>
    <a href="#instanceinitiatedshutdownbehavior" title="InstanceInitiatedShutdownBehavior">InstanceInitiatedShutdownBehavior</a>: <i>String</i>
    <a href="#instancetype" title="InstanceType">InstanceType</a>: <i>String</i>
    <a href="#kernelid" title="KernelId">KernelId</a>: <i>String</i>
    <a href="#keyname" title="KeyName">KeyName</a>: <i>String</i>
    <a href="#latestversion" title="LatestVersion">LatestVersion</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nameprefix" title="NamePrefix">NamePrefix</a>: <i>String</i>
    <a href="#ramdiskid" title="RamDiskId">RamDiskId</a>: <i>String</i>
    <a href="#securitygroupnames" title="SecurityGroupNames">SecurityGroupNames</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#userdata" title="UserData">UserData</a>: <i>String</i>
    <a href="#vpcsecuritygroupids" title="VpcSecurityGroupIds">VpcSecurityGroupIds</a>: <i>
      - String</i>
    <a href="#blockdevicemappings" title="BlockDeviceMappings">BlockDeviceMappings</a>: <i>
      - &lt;a href=&#34;blockdevicemappings.md&#34;&gt;BlockDeviceMappings&lt;/a&gt;</i>
    <a href="#capacityreservationspecification" title="CapacityReservationSpecification">CapacityReservationSpecification</a>: <i>
      - &lt;a href=&#34;capacityreservationspecification.md&#34;&gt;CapacityReservationSpecification&lt;/a&gt;</i>
    <a href="#cpuoptions" title="CpuOptions">CpuOptions</a>: <i>
      - &lt;a href=&#34;cpuoptions.md&#34;&gt;CpuOptions&lt;/a&gt;</i>
    <a href="#creditspecification" title="CreditSpecification">CreditSpecification</a>: <i>
      - &lt;a href=&#34;creditspecification.md&#34;&gt;CreditSpecification&lt;/a&gt;</i>
    <a href="#elasticgpuspecifications" title="ElasticGpuSpecifications">ElasticGpuSpecifications</a>: <i>
      - &lt;a href=&#34;elasticgpuspecifications.md&#34;&gt;ElasticGpuSpecifications&lt;/a&gt;</i>
    <a href="#elasticinferenceaccelerator" title="ElasticInferenceAccelerator">ElasticInferenceAccelerator</a>: <i>
      - &lt;a href=&#34;elasticinferenceaccelerator.md&#34;&gt;ElasticInferenceAccelerator&lt;/a&gt;</i>
    <a href="#iaminstanceprofile" title="IamInstanceProfile">IamInstanceProfile</a>: <i>
      - &lt;a href=&#34;iaminstanceprofile.md&#34;&gt;IamInstanceProfile&lt;/a&gt;</i>
    <a href="#instancemarketoptions" title="InstanceMarketOptions">InstanceMarketOptions</a>: <i>
      - &lt;a href=&#34;instancemarketoptions.md&#34;&gt;InstanceMarketOptions&lt;/a&gt;</i>
    <a href="#licensespecification" title="LicenseSpecification">LicenseSpecification</a>: <i>
      - &lt;a href=&#34;licensespecification.md&#34;&gt;LicenseSpecification&lt;/a&gt;</i>
    <a href="#monitoring" title="Monitoring">Monitoring</a>: <i>
      - &lt;a href=&#34;monitoring.md&#34;&gt;Monitoring&lt;/a&gt;</i>
    <a href="#networkinterfaces" title="NetworkInterfaces">NetworkInterfaces</a>: <i>
      - &lt;a href=&#34;networkinterfaces.md&#34;&gt;NetworkInterfaces&lt;/a&gt;</i>
    <a href="#placement" title="Placement">Placement</a>: <i>
      - &lt;a href=&#34;placement.md&#34;&gt;Placement&lt;/a&gt;</i>
    <a href="#tagspecifications" title="TagSpecifications">TagSpecifications</a>: <i>
      - &lt;a href=&#34;tagspecifications.md&#34;&gt;TagSpecifications&lt;/a&gt;</i>
    <a href="#ebs" title="Ebs">Ebs</a>: <i>
      - &lt;a href=&#34;ebs.md&#34;&gt;Ebs&lt;/a&gt;</i>
    <a href="#capacityreservationtarget" title="CapacityReservationTarget">CapacityReservationTarget</a>: <i>
      - &lt;a href=&#34;capacityreservationtarget.md&#34;&gt;CapacityReservationTarget&lt;/a&gt;</i>
    <a href="#spotoptions" title="SpotOptions">SpotOptions</a>: <i>
      - &lt;a href=&#34;spotoptions.md&#34;&gt;SpotOptions&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Arn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultVersion

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableApiTermination

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EbsOptimized

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceInitiatedShutdownBehavior

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KernelId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LatestVersion

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamePrefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RamDiskId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupNames

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserData

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcSecurityGroupIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockDeviceMappings

_Required_: No

_Type_: List of &lt;a href=&#34;blockdevicemappings.md&#34;&gt;BlockDeviceMappings&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CapacityReservationSpecification

_Required_: No

_Type_: List of &lt;a href=&#34;capacityreservationspecification.md&#34;&gt;CapacityReservationSpecification&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuOptions

_Required_: No

_Type_: List of &lt;a href=&#34;cpuoptions.md&#34;&gt;CpuOptions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreditSpecification

_Required_: No

_Type_: List of &lt;a href=&#34;creditspecification.md&#34;&gt;CreditSpecification&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ElasticGpuSpecifications

_Required_: No

_Type_: List of &lt;a href=&#34;elasticgpuspecifications.md&#34;&gt;ElasticGpuSpecifications&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ElasticInferenceAccelerator

_Required_: No

_Type_: List of &lt;a href=&#34;elasticinferenceaccelerator.md&#34;&gt;ElasticInferenceAccelerator&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IamInstanceProfile

_Required_: No

_Type_: List of &lt;a href=&#34;iaminstanceprofile.md&#34;&gt;IamInstanceProfile&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceMarketOptions

_Required_: No

_Type_: List of &lt;a href=&#34;instancemarketoptions.md&#34;&gt;InstanceMarketOptions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicenseSpecification

_Required_: No

_Type_: List of &lt;a href=&#34;licensespecification.md&#34;&gt;LicenseSpecification&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Monitoring

_Required_: No

_Type_: List of &lt;a href=&#34;monitoring.md&#34;&gt;Monitoring&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkInterfaces

_Required_: No

_Type_: List of &lt;a href=&#34;networkinterfaces.md&#34;&gt;NetworkInterfaces&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Placement

_Required_: No

_Type_: List of &lt;a href=&#34;placement.md&#34;&gt;Placement&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagSpecifications

_Required_: No

_Type_: List of &lt;a href=&#34;tagspecifications.md&#34;&gt;TagSpecifications&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ebs

_Required_: No

_Type_: List of &lt;a href=&#34;ebs.md&#34;&gt;Ebs&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CapacityReservationTarget

_Required_: No

_Type_: List of &lt;a href=&#34;capacityreservationtarget.md&#34;&gt;CapacityReservationTarget&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpotOptions

_Required_: No

_Type_: List of &lt;a href=&#34;spotoptions.md&#34;&gt;SpotOptions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the &lt;code&gt;Arn&lt;/code&gt; value.

#### DefaultVersion

Returns the &lt;code&gt;DefaultVersion&lt;/code&gt; value.

#### LatestVersion

Returns the &lt;code&gt;LatestVersion&lt;/code&gt; value.

