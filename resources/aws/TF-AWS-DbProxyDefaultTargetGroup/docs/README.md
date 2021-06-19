# TF::AWS::DbProxyDefaultTargetGroup

Provides a resource to manage an RDS DB proxy default target group resource.

The `aws_db_proxy_default_target_group` behaves differently from normal resources, in that Terraform does not _create_ or _destroy_ this resource, since it implicitly exists as part of an RDS DB Proxy. On Terraform resource creation it is automatically imported and on resource destruction, Terraform performs no actions in RDS.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::DbProxyDefaultTargetGroup",
    "Properties" : {
        "<a href="#dbproxyname" title="DbProxyName">DbProxyName</a>" : <i>String</i>,
        "<a href="#connectionpoolconfig" title="ConnectionPoolConfig">ConnectionPoolConfig</a>" : <i>[ <a href="connectionpoolconfigdefinition.md">ConnectionPoolConfigDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::DbProxyDefaultTargetGroup
Properties:
    <a href="#dbproxyname" title="DbProxyName">DbProxyName</a>: <i>String</i>
    <a href="#connectionpoolconfig" title="ConnectionPoolConfig">ConnectionPoolConfig</a>: <i>
      - <a href="connectionpoolconfigdefinition.md">ConnectionPoolConfigDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### DbProxyName

Name of the RDS DB Proxy.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionPoolConfig

_Required_: No

_Type_: List of <a href="connectionpoolconfigdefinition.md">ConnectionPoolConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

#### Name

Returns the <code>Name</code> value.

