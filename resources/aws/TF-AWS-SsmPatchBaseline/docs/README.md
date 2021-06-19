# TF::AWS::SsmPatchBaseline

Provides an SSM Patch Baseline resource

~> **NOTE on Patch Baselines:** The `approved_patches` and `approval_rule` are
both marked as optional fields, but the Patch Baseline requires that at least one
of them is specified.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::SsmPatchBaseline",
    "Properties" : {
        "<a href="#approvedpatches" title="ApprovedPatches">ApprovedPatches</a>" : <i>[ String, ... ]</i>,
        "<a href="#approvedpatchescompliancelevel" title="ApprovedPatchesComplianceLevel">ApprovedPatchesComplianceLevel</a>" : <i>String</i>,
        "<a href="#approvedpatchesenablenonsecurity" title="ApprovedPatchesEnableNonSecurity">ApprovedPatchesEnableNonSecurity</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#operatingsystem" title="OperatingSystem">OperatingSystem</a>" : <i>String</i>,
        "<a href="#rejectedpatches" title="RejectedPatches">RejectedPatches</a>" : <i>[ String, ... ]</i>,
        "<a href="#rejectedpatchesaction" title="RejectedPatchesAction">RejectedPatchesAction</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#approvalrule" title="ApprovalRule">ApprovalRule</a>" : <i>[ <a href="approvalruledefinition.md">ApprovalRuleDefinition</a>, ... ]</i>,
        "<a href="#globalfilter" title="GlobalFilter">GlobalFilter</a>" : <i>[ <a href="globalfilterdefinition.md">GlobalFilterDefinition</a>, ... ]</i>,
        "<a href="#source" title="Source">Source</a>" : <i>[ <a href="sourcedefinition.md">SourceDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::SsmPatchBaseline
Properties:
    <a href="#approvedpatches" title="ApprovedPatches">ApprovedPatches</a>: <i>
      - String</i>
    <a href="#approvedpatchescompliancelevel" title="ApprovedPatchesComplianceLevel">ApprovedPatchesComplianceLevel</a>: <i>String</i>
    <a href="#approvedpatchesenablenonsecurity" title="ApprovedPatchesEnableNonSecurity">ApprovedPatchesEnableNonSecurity</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#operatingsystem" title="OperatingSystem">OperatingSystem</a>: <i>String</i>
    <a href="#rejectedpatches" title="RejectedPatches">RejectedPatches</a>: <i>
      - String</i>
    <a href="#rejectedpatchesaction" title="RejectedPatchesAction">RejectedPatchesAction</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#approvalrule" title="ApprovalRule">ApprovalRule</a>: <i>
      - <a href="approvalruledefinition.md">ApprovalRuleDefinition</a></i>
    <a href="#globalfilter" title="GlobalFilter">GlobalFilter</a>: <i>
      - <a href="globalfilterdefinition.md">GlobalFilterDefinition</a></i>
    <a href="#source" title="Source">Source</a>: <i>
      - <a href="sourcedefinition.md">SourceDefinition</a></i>
</pre>

## Properties

#### ApprovedPatches

A list of explicitly approved patches for the baseline.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApprovedPatchesComplianceLevel

Defines the compliance level for approved patches. This means that if an approved patch is reported as missing, this is the severity of the compliance violation. Valid compliance levels include the following: `CRITICAL`, `HIGH`, `MEDIUM`, `LOW`, `INFORMATIONAL`, `UNSPECIFIED`. The default value is `UNSPECIFIED`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApprovedPatchesEnableNonSecurity

Indicates whether the list of approved patches includes non-security updates that should be applied to the instances. Applies to Linux instances only.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description of the patch baseline.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the patch baseline.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OperatingSystem

Defines the operating system the patch baseline applies to. Supported operating systems include `WINDOWS`, `AMAZON_LINUX`, `AMAZON_LINUX_2`, `SUSE`, `UBUNTU`, `CENTOS`, and `REDHAT_ENTERPRISE_LINUX`. The Default value is `WINDOWS`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RejectedPatches

A list of rejected patches.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RejectedPatchesAction

The action for Patch Manager to take on patches included in the `rejected_patches` list. Allow values are `ALLOW_AS_DEPENDENCY` and `BLOCK`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A map of tags to assign to the resource. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApprovalRule

_Required_: No

_Type_: List of <a href="approvalruledefinition.md">ApprovalRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GlobalFilter

_Required_: No

_Type_: List of <a href="globalfilterdefinition.md">GlobalFilterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

_Required_: No

_Type_: List of <a href="sourcedefinition.md">SourceDefinition</a>

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

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

