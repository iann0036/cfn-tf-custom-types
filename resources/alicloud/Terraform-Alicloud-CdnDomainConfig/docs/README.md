# Terraform::Alicloud::CdnDomainConfig

Provides a CDN Accelerated Domain resource.

For information about domain config and how to use it, see [Batch set config](https://www.alibabacloud.com/help/zh/doc-detail/90915.htm)

-> **NOTE:** Available in v1.34.0+.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::CdnDomainConfig",
    "Properties" : {
        "<a href="#domainname" title="DomainName">DomainName</a>" : <i>String</i>,
        "<a href="#functionname" title="FunctionName">FunctionName</a>" : <i>String</i>,
        "<a href="#functionargs" title="FunctionArgs">FunctionArgs</a>" : <i>[ <a href="functionargs.md">FunctionArgs</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::CdnDomainConfig
Properties:
    <a href="#domainname" title="DomainName">DomainName</a>: <i>String</i>
    <a href="#functionname" title="FunctionName">FunctionName</a>: <i>String</i>
    <a href="#functionargs" title="FunctionArgs">FunctionArgs</a>: <i>
      - <a href="functionargs.md">FunctionArgs</a></i>
</pre>

## Properties

#### DomainName

Name of the accelerated domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or "-", and must not begin or end with "-", and "-" must not in the 3th and 4th character positions at the same time. Suffix `.sh` and `.tel` are not supported.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FunctionName

The name of the domain config.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FunctionArgs

_Required_: No

_Type_: List of <a href="functionargs.md">FunctionArgs</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

