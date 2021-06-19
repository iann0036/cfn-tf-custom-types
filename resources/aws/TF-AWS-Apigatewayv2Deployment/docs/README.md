# TF::AWS::Apigatewayv2Deployment

Manages an Amazon API Gateway Version 2 deployment.
More information can be found in the [Amazon API Gateway Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api.html).

-> **Note:** Creating a deployment for an API requires at least one `aws_apigatewayv2_route` resource associated with that API. To avoid race conditions when all resources are being created together, you need to add implicit resource references via the `triggers` argument or explicit resource references using the [resource `depends_on` meta-argument](https://www.terraform.io/docs/configuration/meta-arguments/depends_on.html).

-> It is recommended to enable the [resource `lifecycle` configuration block `create_before_destroy` argument](https://www.terraform.io/docs/configuration/resources.html#create_before_destroy) in this resource configuration to properly order redeployments in Terraform.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::Apigatewayv2Deployment",
    "Properties" : {
        "<a href="#apiid" title="ApiId">ApiId</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#triggers" title="Triggers">Triggers</a>" : <i>[ <a href="triggersdefinition.md">TriggersDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::Apigatewayv2Deployment
Properties:
    <a href="#apiid" title="ApiId">ApiId</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#triggers" title="Triggers">Triggers</a>: <i>
      - <a href="triggersdefinition.md">TriggersDefinition</a></i>
</pre>

## Properties

#### ApiId

The API identifier.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description for the deployment resource. Must be less than or equal to 1024 characters in length.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Triggers

A map of arbitrary keys and values that, when changed, will trigger a redeployment. To force a redeployment without changing these keys/values, use the [`terraform taint` command](https://www.terraform.io/docs/commands/taint.html).

_Required_: No

_Type_: List of <a href="triggersdefinition.md">TriggersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AutoDeployed

Returns the <code>AutoDeployed</code> value.

#### Id

Returns the <code>Id</code> value.

