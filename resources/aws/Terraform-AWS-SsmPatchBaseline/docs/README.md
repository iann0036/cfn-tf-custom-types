# Terraform::AWS::SsmPatchBaseline

CloudFormation equivalent of aws_ssm_patch_baseline

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::SsmPatchBaseline",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#approvedpatches" title="ApprovedPatches">ApprovedPatches</a>" : <i>[ String, ... ]</i>,
        "<a href="#approvedpatchescompliancelevel" title="ApprovedPatchesComplianceLevel">ApprovedPatchesComplianceLevel</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#operatingsystem" title="OperatingSystem">OperatingSystem</a>" : <i>String</i>,
        "<a href="#rejectedpatches" title="RejectedPatches">RejectedPatches</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#approvalrule" title="ApprovalRule">ApprovalRule</a>" : <i>[ &lt;a href=&#34;approvalrule.md&#34;&gt;ApprovalRule&lt;/a&gt;, ... ]</i>,
        "<a href="#globalfilter" title="GlobalFilter">GlobalFilter</a>" : <i>[ &lt;a href=&#34;globalfilter.md&#34;&gt;GlobalFilter&lt;/a&gt;, ... ]</i>,
        "<a href="#patchfilter" title="PatchFilter">PatchFilter</a>" : <i>[ &lt;a href=&#34;patchfilter.md&#34;&gt;PatchFilter&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::SsmPatchBaseline
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#approvedpatches" title="ApprovedPatches">ApprovedPatches</a>: <i>
      - String</i>
    <a href="#approvedpatchescompliancelevel" title="ApprovedPatchesComplianceLevel">ApprovedPatchesComplianceLevel</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#operatingsystem" title="OperatingSystem">OperatingSystem</a>: <i>String</i>
    <a href="#rejectedpatches" title="RejectedPatches">RejectedPatches</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#approvalrule" title="ApprovalRule">ApprovalRule</a>: <i>
      - &lt;a href=&#34;approvalrule.md&#34;&gt;ApprovalRule&lt;/a&gt;</i>
    <a href="#globalfilter" title="GlobalFilter">GlobalFilter</a>: <i>
      - &lt;a href=&#34;globalfilter.md&#34;&gt;GlobalFilter&lt;/a&gt;</i>
    <a href="#patchfilter" title="PatchFilter">PatchFilter</a>: <i>
      - &lt;a href=&#34;patchfilter.md&#34;&gt;PatchFilter&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApprovedPatches

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApprovedPatchesComplianceLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OperatingSystem

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RejectedPatches

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApprovalRule

_Required_: No

_Type_: List of &lt;a href=&#34;approvalrule.md&#34;&gt;ApprovalRule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GlobalFilter

_Required_: No

_Type_: List of &lt;a href=&#34;globalfilter.md&#34;&gt;GlobalFilter&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PatchFilter

_Required_: No

_Type_: List of &lt;a href=&#34;patchfilter.md&#34;&gt;PatchFilter&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

