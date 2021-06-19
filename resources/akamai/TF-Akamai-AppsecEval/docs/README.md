# TF::Akamai::AppsecEval

Use the `akamai_appsec_eval` resource to perform evaluation mode operations such as Start, Stop, Restart, Update, or Complete.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Akamai::AppsecEval",
    "Properties" : {
        "<a href="#configid" title="ConfigId">ConfigId</a>" : <i>Double</i>,
        "<a href="#evaloperation" title="EvalOperation">EvalOperation</a>" : <i>String</i>,
        "<a href="#securitypolicyid" title="SecurityPolicyId">SecurityPolicyId</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Akamai::AppsecEval
Properties:
    <a href="#configid" title="ConfigId">ConfigId</a>: <i>Double</i>
    <a href="#evaloperation" title="EvalOperation">EvalOperation</a>: <i>String</i>
    <a href="#securitypolicyid" title="SecurityPolicyId">SecurityPolicyId</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>Double</i>
</pre>

## Properties

#### ConfigId

The ID of the security configuration to use.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EvalOperation

The operation to perform: START, STOP, RESTART, UPDATE, or COMPLETE.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityPolicyId

The ID of the security policy to use.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

The version number of the security configuration to use.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CurrentRuleset

Returns the <code>CurrentRuleset</code> value.

#### EvalStatus

Returns the <code>EvalStatus</code> value.

#### EvaluatingRuleset

Returns the <code>EvaluatingRuleset</code> value.

#### ExpirationDate

Returns the <code>ExpirationDate</code> value.

#### Id

Returns the <code>Id</code> value.

#### OutputText

Returns the <code>OutputText</code> value.

