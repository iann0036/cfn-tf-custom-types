# TF::Nutanix::RecoveryPlan ParametersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#floatingipassignmentlist" title="FloatingIpAssignmentList">FloatingIpAssignmentList</a>" : <i>[ <a href="floatingipassignmentlistdefinition.md">FloatingIpAssignmentListDefinition</a>, ... ]</i>,
    "<a href="#networkmappinglist" title="NetworkMappingList">NetworkMappingList</a>" : <i>[ <a href="networkmappinglistdefinition.md">NetworkMappingListDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#floatingipassignmentlist" title="FloatingIpAssignmentList">FloatingIpAssignmentList</a>: <i>
      - <a href="floatingipassignmentlistdefinition.md">FloatingIpAssignmentListDefinition</a></i>
<a href="#networkmappinglist" title="NetworkMappingList">NetworkMappingList</a>: <i>
      - <a href="networkmappinglistdefinition.md">NetworkMappingListDefinition</a></i>
</pre>

## Properties

#### FloatingIpAssignmentList

_Required_: No

_Type_: List of <a href="floatingipassignmentlistdefinition.md">FloatingIpAssignmentListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkMappingList

_Required_: No

_Type_: List of <a href="networkmappinglistdefinition.md">NetworkMappingListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

