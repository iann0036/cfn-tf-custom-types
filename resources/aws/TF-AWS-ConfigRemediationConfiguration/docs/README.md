# TF::AWS::ConfigRemediationConfiguration

Provides an AWS Config Remediation Configuration.

~> **Note:** Config Remediation Configuration requires an existing [Config Rule](/docs/providers/aws/r/config_config_rule.html) to be present.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::ConfigRemediationConfiguration",
    "Properties" : {
        "<a href="#configrulename" title="ConfigRuleName">ConfigRuleName</a>" : <i>String</i>,
        "<a href="#resourcetype" title="ResourceType">ResourceType</a>" : <i>String</i>,
        "<a href="#targetid" title="TargetId">TargetId</a>" : <i>String</i>,
        "<a href="#targettype" title="TargetType">TargetType</a>" : <i>String</i>,
        "<a href="#targetversion" title="TargetVersion">TargetVersion</a>" : <i>String</i>,
        "<a href="#parameter" title="Parameter">Parameter</a>" : <i>[ <a href="parameterdefinition.md">ParameterDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::ConfigRemediationConfiguration
Properties:
    <a href="#configrulename" title="ConfigRuleName">ConfigRuleName</a>: <i>String</i>
    <a href="#resourcetype" title="ResourceType">ResourceType</a>: <i>String</i>
    <a href="#targetid" title="TargetId">TargetId</a>: <i>String</i>
    <a href="#targettype" title="TargetType">TargetType</a>: <i>String</i>
    <a href="#targetversion" title="TargetVersion">TargetVersion</a>: <i>String</i>
    <a href="#parameter" title="Parameter">Parameter</a>: <i>
      - <a href="parameterdefinition.md">ParameterDefinition</a></i>
</pre>

## Properties

#### ConfigRuleName

The name of the AWS Config rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceType

The type of a resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetId

Target ID is the name of the public document.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetType

The type of the target. Target executes remediation. For example, SSM document.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetVersion

Version of the target. For example, version of the SSM document.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parameter

_Required_: No

_Type_: List of <a href="parameterdefinition.md">ParameterDefinition</a>

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

