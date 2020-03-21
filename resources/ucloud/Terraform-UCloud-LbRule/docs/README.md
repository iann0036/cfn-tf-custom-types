# Terraform::UCloud::LbRule

Provides a Load Balancer Rule resource to add content forwarding policies for Load Balancer backend resource.
 
~> **Note** The Load Balancer Rule can only be define while the `protocol` of lb listener is one of HTTP and HTTPS. In addition, should set one of `domain` and `path` if defined.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::UCloud::LbRule",
    "Properties" : {
        "<a href="#backendids" title="BackendIds">BackendIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#listenerid" title="ListenerId">ListenerId</a>" : <i>String</i>,
        "<a href="#loadbalancerid" title="LoadBalancerId">LoadBalancerId</a>" : <i>String</i>,
        "<a href="#path" title="Path">Path</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::UCloud::LbRule
Properties:
    <a href="#backendids" title="BackendIds">BackendIds</a>: <i>
      - String</i>
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#listenerid" title="ListenerId">ListenerId</a>: <i>String</i>
    <a href="#loadbalancerid" title="LoadBalancerId">LoadBalancerId</a>: <i>String</i>
    <a href="#path" title="Path">Path</a>: <i>String</i>
</pre>

## Properties

#### BackendIds

The IDs of the backend servers where rule applies, this argument is populated base on the `backend_id` responded from `lb_attachment` create.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

The domain of content forward matching fields. `path` and `domain` cannot coexist. `path` and `domain` must be filled in one.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ListenerId

The ID of a listener server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerId

The ID of a load balancer.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

The path of Content forward matching fields. `path` and `domain` cannot coexist. `path` and `domain` must be filled in one.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

