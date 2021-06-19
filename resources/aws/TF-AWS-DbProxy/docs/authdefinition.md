# TF::AWS::DbProxy AuthDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#authscheme" title="AuthScheme">AuthScheme</a>" : <i>String</i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#iamauth" title="IamAuth">IamAuth</a>" : <i>String</i>,
    "<a href="#secretarn" title="SecretArn">SecretArn</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#authscheme" title="AuthScheme">AuthScheme</a>: <i>String</i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#iamauth" title="IamAuth">IamAuth</a>: <i>String</i>
<a href="#secretarn" title="SecretArn">SecretArn</a>: <i>String</i>
</pre>

## Properties

#### AuthScheme

The type of authentication that the proxy uses for connections from the proxy to the underlying database. One of `SECRETS`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A user-specified description about the authentication used by a proxy to log in as a specific database user.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IamAuth

Whether to require or disallow AWS Identity and Access Management (IAM) authentication for connections to the proxy. One of `DISABLED`, `REQUIRED`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretArn

The Amazon Resource Name (ARN) representing the secret that the proxy uses to authenticate to the RDS DB instance or Aurora DB cluster. These secrets are stored within Amazon Secrets Manager.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

