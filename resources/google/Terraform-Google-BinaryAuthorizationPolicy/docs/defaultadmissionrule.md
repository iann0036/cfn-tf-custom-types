# Terraform::Google::BinaryAuthorizationPolicy DefaultAdmissionRule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enforcementmode" title="EnforcementMode">EnforcementMode</a>" : <i>String</i>,
    "<a href="#evaluationmode" title="EvaluationMode">EvaluationMode</a>" : <i>String</i>,
    "<a href="#requireattestationsby" title="RequireAttestationsBy">RequireAttestationsBy</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#enforcementmode" title="EnforcementMode">EnforcementMode</a>: <i>String</i>
<a href="#evaluationmode" title="EvaluationMode">EvaluationMode</a>: <i>String</i>
<a href="#requireattestationsby" title="RequireAttestationsBy">RequireAttestationsBy</a>: <i>
      - String</i>
</pre>

## Properties

#### EnforcementMode

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EvaluationMode

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequireAttestationsBy

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

