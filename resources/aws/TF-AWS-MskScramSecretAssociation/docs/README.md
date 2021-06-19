# TF::AWS::MskScramSecretAssociation

Associates SCRAM secrets stored in the Secrets Manager service with a Managed Streaming for Kafka (MSK) cluster.

-> **Note:** The following assumes the MSK cluster has SASL/SCRAM authentication enabled. See below for example usage or refer to the [Username/Password Authentication](https://docs.aws.amazon.com/msk/latest/developerguide/msk-password.html) section of the MSK Developer Guide for more details.

To set up username and password authentication for a cluster, create an [`aws_secretsmanager_secret` resource](/docs/providers/aws/r/secretsmanager_secret.html) and associate
a username and password with the secret with an [`aws_secretsmanager_secret_version` resource](/docs/providers/aws/r/secretsmanager_secret_version.html). When creating a secret for the cluster,
the `name` must have the prefix `AmazonMSK_` and you must either use an existing custom AWS KMS key or create a new
custom AWS KMS key for your secret with the [`aws_kms_key` resource](/docs/providers/aws/r/kms_key.html). It is important to ...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::MskScramSecretAssociation",
    "Properties" : {
        "<a href="#clusterarn" title="ClusterArn">ClusterArn</a>" : <i>String</i>,
        "<a href="#secretarnlist" title="SecretArnList">SecretArnList</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::MskScramSecretAssociation
Properties:
    <a href="#clusterarn" title="ClusterArn">ClusterArn</a>: <i>String</i>
    <a href="#secretarnlist" title="SecretArnList">SecretArnList</a>: <i>
      - String</i>
</pre>

## Properties

#### ClusterArn

Amazon Resource Name (ARN) of the MSK cluster.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretArnList

List of AWS Secrets Manager secret ARNs.

_Required_: Yes

_Type_: List of String

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

