# Terraform::OCI::ApigatewayDeployment

This resource provides the Deployment resource in Oracle Cloud Infrastructure API Gateway service.

Creates a new deployment.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::ApigatewayDeployment",
    "Properties" : {
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="definedtags.md">DefinedTags</a>, ... ]</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="freeformtags.md">FreeformTags</a>, ... ]</i>,
        "<a href="#gatewayid" title="GatewayId">GatewayId</a>" : <i>String</i>,
        "<a href="#pathprefix" title="PathPrefix">PathPrefix</a>" : <i>String</i>,
        "<a href="#specification" title="Specification">Specification</a>" : <i>[ <a href="specification.md">Specification</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#loggingpolicies" title="LoggingPolicies">LoggingPolicies</a>" : <i>[ <a href="loggingpolicies.md">LoggingPolicies</a>, ... ]</i>,
        "<a href="#requestpolicies" title="RequestPolicies">RequestPolicies</a>" : <i>[ <a href="requestpolicies.md">RequestPolicies</a>, ... ]</i>,
        "<a href="#routes" title="Routes">Routes</a>" : <i>[ <a href="routes.md">Routes</a>, ... ]</i>,
        "<a href="#accesslog" title="AccessLog">AccessLog</a>" : <i>[ <a href="accesslog.md">AccessLog</a>, ... ]</i>,
        "<a href="#executionlog" title="ExecutionLog">ExecutionLog</a>" : <i>[ <a href="executionlog.md">ExecutionLog</a>, ... ]</i>,
        "<a href="#authentication" title="Authentication">Authentication</a>" : <i>[ <a href="authentication.md">Authentication</a>, ... ]</i>,
        "<a href="#cors" title="Cors">Cors</a>" : <i>[ <a href="cors.md">Cors</a>, ... ]</i>,
        "<a href="#ratelimiting" title="RateLimiting">RateLimiting</a>" : <i>[ <a href="ratelimiting.md">RateLimiting</a>, ... ]</i>,
        "<a href="#backend" title="Backend">Backend</a>" : <i>[ <a href="backend.md">Backend</a>, ... ]</i>,
        "<a href="#headers" title="Headers">Headers</a>" : <i>[ <a href="headers.md">Headers</a>, ... ]</i>,
        "<a href="#authorization" title="Authorization">Authorization</a>" : <i>[ <a href="authorization.md">Authorization</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::ApigatewayDeployment
Properties:
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - <a href="definedtags.md">DefinedTags</a></i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="freeformtags.md">FreeformTags</a></i>
    <a href="#gatewayid" title="GatewayId">GatewayId</a>: <i>String</i>
    <a href="#pathprefix" title="PathPrefix">PathPrefix</a>: <i>String</i>
    <a href="#specification" title="Specification">Specification</a>: <i>
      - <a href="specification.md">Specification</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#loggingpolicies" title="LoggingPolicies">LoggingPolicies</a>: <i>
      - <a href="loggingpolicies.md">LoggingPolicies</a></i>
    <a href="#requestpolicies" title="RequestPolicies">RequestPolicies</a>: <i>
      - <a href="requestpolicies.md">RequestPolicies</a></i>
    <a href="#routes" title="Routes">Routes</a>: <i>
      - <a href="routes.md">Routes</a></i>
    <a href="#accesslog" title="AccessLog">AccessLog</a>: <i>
      - <a href="accesslog.md">AccessLog</a></i>
    <a href="#executionlog" title="ExecutionLog">ExecutionLog</a>: <i>
      - <a href="executionlog.md">ExecutionLog</a></i>
    <a href="#authentication" title="Authentication">Authentication</a>: <i>
      - <a href="authentication.md">Authentication</a></i>
    <a href="#cors" title="Cors">Cors</a>: <i>
      - <a href="cors.md">Cors</a></i>
    <a href="#ratelimiting" title="RateLimiting">RateLimiting</a>: <i>
      - <a href="ratelimiting.md">RateLimiting</a></i>
    <a href="#backend" title="Backend">Backend</a>: <i>
      - <a href="backend.md">Backend</a></i>
    <a href="#headers" title="Headers">Headers</a>: <i>
      - <a href="headers.md">Headers</a></i>
    <a href="#authorization" title="Authorization">Authorization</a>: <i>
      - <a href="authorization.md">Authorization</a></i>
</pre>

## Properties

#### CompartmentId

(Updatable) The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment in which the resource is created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

(Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Operations.CostCenter": "42"}`.

_Required_: No

_Type_: List of <a href="definedtags.md">DefinedTags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

(Updatable) A user-friendly name. Does not have to be unique, and it's changeable.  Avoid entering confidential information.  Example: `My new resource`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

(Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

_Required_: No

_Type_: List of <a href="freeformtags.md">FreeformTags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayId

The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PathPrefix

A path on which to deploy all routes contained in the API deployment specification. For more information, see [Deploying an API on an API Gateway by Creating an API  Deployment](https://docs.cloud.oracle.com/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Specification

_Required_: No

_Type_: List of <a href="specification.md">Specification</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingPolicies

_Required_: No

_Type_: List of <a href="loggingpolicies.md">LoggingPolicies</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestPolicies

_Required_: No

_Type_: List of <a href="requestpolicies.md">RequestPolicies</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Routes

_Required_: No

_Type_: List of <a href="routes.md">Routes</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessLog

_Required_: No

_Type_: List of <a href="accesslog.md">AccessLog</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExecutionLog

_Required_: No

_Type_: List of <a href="executionlog.md">ExecutionLog</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Authentication

_Required_: No

_Type_: List of <a href="authentication.md">Authentication</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cors

_Required_: No

_Type_: List of <a href="cors.md">Cors</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RateLimiting

_Required_: No

_Type_: List of <a href="ratelimiting.md">RateLimiting</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Backend

_Required_: No

_Type_: List of <a href="backend.md">Backend</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Headers

_Required_: No

_Type_: List of <a href="headers.md">Headers</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Authorization

_Required_: No

_Type_: List of <a href="authorization.md">Authorization</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Endpoint

Returns the <code>Endpoint</code> value.

#### Id

Returns the <code>Id</code> value.

#### LifecycleDetails

Returns the <code>LifecycleDetails</code> value.

#### State

Returns the <code>State</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

#### TimeUpdated

Returns the <code>TimeUpdated</code> value.

