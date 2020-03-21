# Terraform::AWS::SsmAssociation

CloudFormation equivalent of aws_ssm_association

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::SsmAssociation",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#associationid" title="AssociationId">AssociationId</a>" : <i>String</i>,
        "<a href="#associationname" title="AssociationName">AssociationName</a>" : <i>String</i>,
        "<a href="#automationtargetparametername" title="AutomationTargetParameterName">AutomationTargetParameterName</a>" : <i>String</i>,
        "<a href="#complianceseverity" title="ComplianceSeverity">ComplianceSeverity</a>" : <i>String</i>,
        "<a href="#documentversion" title="DocumentVersion">DocumentVersion</a>" : <i>String</i>,
        "<a href="#instanceid" title="InstanceId">InstanceId</a>" : <i>String</i>,
        "<a href="#maxconcurrency" title="MaxConcurrency">MaxConcurrency</a>" : <i>String</i>,
        "<a href="#maxerrors" title="MaxErrors">MaxErrors</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#parameters" title="Parameters">Parameters</a>" : <i>[ &lt;a href=&#34;parameters.md&#34;&gt;Parameters&lt;/a&gt;, ... ]</i>,
        "<a href="#scheduleexpression" title="ScheduleExpression">ScheduleExpression</a>" : <i>String</i>,
        "<a href="#outputlocation" title="OutputLocation">OutputLocation</a>" : <i>[ &lt;a href=&#34;outputlocation.md&#34;&gt;OutputLocation&lt;/a&gt;, ... ]</i>,
        "<a href="#targets" title="Targets">Targets</a>" : <i>[ &lt;a href=&#34;targets.md&#34;&gt;Targets&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::SsmAssociation
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#associationid" title="AssociationId">AssociationId</a>: <i>String</i>
    <a href="#associationname" title="AssociationName">AssociationName</a>: <i>String</i>
    <a href="#automationtargetparametername" title="AutomationTargetParameterName">AutomationTargetParameterName</a>: <i>String</i>
    <a href="#complianceseverity" title="ComplianceSeverity">ComplianceSeverity</a>: <i>String</i>
    <a href="#documentversion" title="DocumentVersion">DocumentVersion</a>: <i>String</i>
    <a href="#instanceid" title="InstanceId">InstanceId</a>: <i>String</i>
    <a href="#maxconcurrency" title="MaxConcurrency">MaxConcurrency</a>: <i>String</i>
    <a href="#maxerrors" title="MaxErrors">MaxErrors</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#parameters" title="Parameters">Parameters</a>: <i>
      - &lt;a href=&#34;parameters.md&#34;&gt;Parameters&lt;/a&gt;</i>
    <a href="#scheduleexpression" title="ScheduleExpression">ScheduleExpression</a>: <i>String</i>
    <a href="#outputlocation" title="OutputLocation">OutputLocation</a>: <i>
      - &lt;a href=&#34;outputlocation.md&#34;&gt;OutputLocation&lt;/a&gt;</i>
    <a href="#targets" title="Targets">Targets</a>: <i>
      - &lt;a href=&#34;targets.md&#34;&gt;Targets&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssociationId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssociationName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutomationTargetParameterName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ComplianceSeverity

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DocumentVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxConcurrency

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxErrors

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parameters

_Required_: No

_Type_: List of &lt;a href=&#34;parameters.md&#34;&gt;Parameters&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduleExpression

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutputLocation

_Required_: No

_Type_: List of &lt;a href=&#34;outputlocation.md&#34;&gt;OutputLocation&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Targets

_Required_: No

_Type_: List of &lt;a href=&#34;targets.md&#34;&gt;Targets&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AssociationId

Returns the &lt;code&gt;AssociationId&lt;/code&gt; value.

