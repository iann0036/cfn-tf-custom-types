# Terraform::AWS::SsmPatchBaseline ApprovalRule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#approveafterdays" title="ApproveAfterDays">ApproveAfterDays</a>" : <i>Double</i>,
    "<a href="#compliancelevel" title="ComplianceLevel">ComplianceLevel</a>" : <i>String</i>,
    "<a href="#enablenonsecurity" title="EnableNonSecurity">EnableNonSecurity</a>" : <i>Boolean</i>,
    "<a href="#patchfilter" title="PatchFilter">PatchFilter</a>" : <i>[ <a href="approvalrule-patchfilter.md">PatchFilter</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#approveafterdays" title="ApproveAfterDays">ApproveAfterDays</a>: <i>Double</i>
<a href="#compliancelevel" title="ComplianceLevel">ComplianceLevel</a>: <i>String</i>
<a href="#enablenonsecurity" title="EnableNonSecurity">EnableNonSecurity</a>: <i>Boolean</i>
<a href="#patchfilter" title="PatchFilter">PatchFilter</a>: <i>
      - <a href="approvalrule-patchfilter.md">PatchFilter</a></i>
</pre>

## Properties

#### ApproveAfterDays

The number of days after the release date of each patch matched by the rule the patch is marked as approved in the patch baseline. Valid Range: 0 to 100.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ComplianceLevel

Defines the compliance level for patches approved by this rule. Valid compliance levels include the following: `CRITICAL`, `HIGH`, `MEDIUM`, `LOW`, `INFORMATIONAL`, `UNSPECIFIED`. The default value is `UNSPECIFIED`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableNonSecurity

Boolean enabling the application of non-security updates. The default value is 'false'. Valid for Linux instances only.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PatchFilter

_Required_: No

_Type_: List of <a href="approvalrule-patchfilter.md">PatchFilter</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

