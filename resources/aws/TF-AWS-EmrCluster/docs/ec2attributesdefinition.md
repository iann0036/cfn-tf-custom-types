# TF::AWS::EmrCluster Ec2AttributesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#additionalmastersecuritygroups" title="AdditionalMasterSecurityGroups">AdditionalMasterSecurityGroups</a>" : <i>String</i>,
    "<a href="#additionalslavesecuritygroups" title="AdditionalSlaveSecurityGroups">AdditionalSlaveSecurityGroups</a>" : <i>String</i>,
    "<a href="#emrmanagedmastersecuritygroup" title="EmrManagedMasterSecurityGroup">EmrManagedMasterSecurityGroup</a>" : <i>String</i>,
    "<a href="#emrmanagedslavesecuritygroup" title="EmrManagedSlaveSecurityGroup">EmrManagedSlaveSecurityGroup</a>" : <i>String</i>,
    "<a href="#instanceprofile" title="InstanceProfile">InstanceProfile</a>" : <i>String</i>,
    "<a href="#keyname" title="KeyName">KeyName</a>" : <i>String</i>,
    "<a href="#serviceaccesssecuritygroup" title="ServiceAccessSecurityGroup">ServiceAccessSecurityGroup</a>" : <i>String</i>,
    "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
    "<a href="#subnetids" title="SubnetIds">SubnetIds</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#additionalmastersecuritygroups" title="AdditionalMasterSecurityGroups">AdditionalMasterSecurityGroups</a>: <i>String</i>
<a href="#additionalslavesecuritygroups" title="AdditionalSlaveSecurityGroups">AdditionalSlaveSecurityGroups</a>: <i>String</i>
<a href="#emrmanagedmastersecuritygroup" title="EmrManagedMasterSecurityGroup">EmrManagedMasterSecurityGroup</a>: <i>String</i>
<a href="#emrmanagedslavesecuritygroup" title="EmrManagedSlaveSecurityGroup">EmrManagedSlaveSecurityGroup</a>: <i>String</i>
<a href="#instanceprofile" title="InstanceProfile">InstanceProfile</a>: <i>String</i>
<a href="#keyname" title="KeyName">KeyName</a>: <i>String</i>
<a href="#serviceaccesssecuritygroup" title="ServiceAccessSecurityGroup">ServiceAccessSecurityGroup</a>: <i>String</i>
<a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
<a href="#subnetids" title="SubnetIds">SubnetIds</a>: <i>
      - String</i>
</pre>

## Properties

#### AdditionalMasterSecurityGroups

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdditionalSlaveSecurityGroups

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmrManagedMasterSecurityGroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmrManagedSlaveSecurityGroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceProfile

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceAccessSecurityGroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

