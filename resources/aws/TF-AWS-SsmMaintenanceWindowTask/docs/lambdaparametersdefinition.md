# TF::AWS::SsmMaintenanceWindowTask LambdaParametersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#clientcontext" title="ClientContext">ClientContext</a>" : <i>String</i>,
    "<a href="#payload" title="Payload">Payload</a>" : <i>String</i>,
    "<a href="#qualifier" title="Qualifier">Qualifier</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#clientcontext" title="ClientContext">ClientContext</a>: <i>String</i>
<a href="#payload" title="Payload">Payload</a>: <i>String</i>
<a href="#qualifier" title="Qualifier">Qualifier</a>: <i>String</i>
</pre>

## Properties

#### ClientContext

Pass client-specific information to the Lambda function that you are invoking.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Payload

JSON to provide to your Lambda function as input.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Qualifier

Specify a Lambda function version or alias name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

