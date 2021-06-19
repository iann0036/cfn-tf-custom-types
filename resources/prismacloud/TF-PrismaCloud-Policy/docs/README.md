# TF::PrismaCloud::Policy

Manage a specific policy.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::PrismaCloud::Policy",
    "Properties" : {
        "<a href="#cloudtype" title="CloudType">CloudType</a>" : <i>String</i>,
        "<a href="#deleted" title="Deleted">Deleted</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#overridden" title="Overridden">Overridden</a>" : <i>Boolean</i>,
        "<a href="#policytype" title="PolicyType">PolicyType</a>" : <i>String</i>,
        "<a href="#recommendation" title="Recommendation">Recommendation</a>" : <i>String</i>,
        "<a href="#remediable" title="Remediable">Remediable</a>" : <i>Boolean</i>,
        "<a href="#restrictalertdismissal" title="RestrictAlertDismissal">RestrictAlertDismissal</a>" : <i>Boolean</i>,
        "<a href="#severity" title="Severity">Severity</a>" : <i>String</i>,
        "<a href="#systemdefault" title="SystemDefault">SystemDefault</a>" : <i>Boolean</i>,
        "<a href="#compliancemetadata" title="ComplianceMetadata">ComplianceMetadata</a>" : <i>[ <a href="compliancemetadatadefinition.md">ComplianceMetadataDefinition</a>, ... ]</i>,
        "<a href="#remediation" title="Remediation">Remediation</a>" : <i>[ <a href="remediationdefinition.md">RemediationDefinition</a>, ... ]</i>,
        "<a href="#rule" title="Rule">Rule</a>" : <i>[ <a href="ruledefinition.md">RuleDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::PrismaCloud::Policy
Properties:
    <a href="#cloudtype" title="CloudType">CloudType</a>: <i>String</i>
    <a href="#deleted" title="Deleted">Deleted</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#overridden" title="Overridden">Overridden</a>: <i>Boolean</i>
    <a href="#policytype" title="PolicyType">PolicyType</a>: <i>String</i>
    <a href="#recommendation" title="Recommendation">Recommendation</a>: <i>String</i>
    <a href="#remediable" title="Remediable">Remediable</a>: <i>Boolean</i>
    <a href="#restrictalertdismissal" title="RestrictAlertDismissal">RestrictAlertDismissal</a>: <i>Boolean</i>
    <a href="#severity" title="Severity">Severity</a>: <i>String</i>
    <a href="#systemdefault" title="SystemDefault">SystemDefault</a>: <i>Boolean</i>
    <a href="#compliancemetadata" title="ComplianceMetadata">ComplianceMetadata</a>: <i>
      - <a href="compliancemetadatadefinition.md">ComplianceMetadataDefinition</a></i>
    <a href="#remediation" title="Remediation">Remediation</a>: <i>
      - <a href="remediationdefinition.md">RemediationDefinition</a></i>
    <a href="#rule" title="Rule">Rule</a>: <i>
      - <a href="ruledefinition.md">RuleDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### CloudType

Cloud type.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Deleted

Deleted.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

List of labels.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Policy name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Overridden

Overridden.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyType

Policy type.  Valid values are `config`, `audit_event`, or `network`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Recommendation

Remediation recommendation.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Remediable

Is remediable or not.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestrictAlertDismissal

Restrict alert dismissal.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Severity

Severity.  Valid values are `low` (default), `medium`, or `high`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SystemDefault

If policy is a system default policy or not.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ComplianceMetadata

_Required_: No

_Type_: List of <a href="compliancemetadatadefinition.md">ComplianceMetadataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Remediation

_Required_: No

_Type_: List of <a href="remediationdefinition.md">RemediationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rule

_Required_: No

_Type_: List of <a href="ruledefinition.md">RuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreatedBy

Returns the <code>CreatedBy</code> value.

#### CreatedOn

Returns the <code>CreatedOn</code> value.

#### Id

Returns the <code>Id</code> value.

#### LastModifiedBy

Returns the <code>LastModifiedBy</code> value.

#### LastModifiedOn

Returns the <code>LastModifiedOn</code> value.

#### OpenAlertsCount

Returns the <code>OpenAlertsCount</code> value.

#### Owner

Returns the <code>Owner</code> value.

#### PolicyId

Returns the <code>PolicyId</code> value.

#### PolicyMode

Returns the <code>PolicyMode</code> value.

#### RuleLastModifiedOn

Returns the <code>RuleLastModifiedOn</code> value.

