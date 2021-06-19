# TF::AWS::SecretsmanagerSecretRotation

Provides a resource to manage AWS Secrets Manager secret rotation. To manage a secret, see the [`aws_secretsmanager_secret` resource](/docs/providers/aws/r/secretsmanager_secret.html). To manage a secret value, see the [`aws_secretsmanager_secret_version` resource](/docs/providers/aws/r/secretsmanager_secret_version.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::SecretsmanagerSecretRotation",
    "Properties" : {
        "<a href="#rotationlambdaarn" title="RotationLambdaArn">RotationLambdaArn</a>" : <i>String</i>,
        "<a href="#secretid" title="SecretId">SecretId</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#rotationrules" title="RotationRules">RotationRules</a>" : <i>[ <a href="rotationrulesdefinition.md">RotationRulesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::SecretsmanagerSecretRotation
Properties:
    <a href="#rotationlambdaarn" title="RotationLambdaArn">RotationLambdaArn</a>: <i>String</i>
    <a href="#secretid" title="SecretId">SecretId</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#rotationrules" title="RotationRules">RotationRules</a>: <i>
      - <a href="rotationrulesdefinition.md">RotationRulesDefinition</a></i>
</pre>

## Properties

#### RotationLambdaArn

Specifies the ARN of the Lambda function that can rotate the secret.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretId

Specifies the secret to which you want to add a new version. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret. The secret must already exist.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RotationRules

_Required_: No

_Type_: List of <a href="rotationrulesdefinition.md">RotationRulesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### RotationEnabled

Returns the <code>RotationEnabled</code> value.

