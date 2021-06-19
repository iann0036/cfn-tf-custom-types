# TF::Nutanix::RecoveryPlan FloatingIpAssignmentListDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#availabilityzoneurl" title="AvailabilityZoneUrl">AvailabilityZoneUrl</a>" : <i>String</i>,
    "<a href="#vmipassignmentlist" title="VmIpAssignmentList">VmIpAssignmentList</a>" : <i>[ <a href="vmipassignmentlistdefinition.md">VmIpAssignmentListDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#availabilityzoneurl" title="AvailabilityZoneUrl">AvailabilityZoneUrl</a>: <i>String</i>
<a href="#vmipassignmentlist" title="VmIpAssignmentList">VmIpAssignmentList</a>: <i>
      - <a href="vmipassignmentlistdefinition.md">VmIpAssignmentListDefinition</a></i>
</pre>

## Properties

#### AvailabilityZoneUrl

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmIpAssignmentList

_Required_: No

_Type_: List of <a href="vmipassignmentlistdefinition.md">VmIpAssignmentListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

