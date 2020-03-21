# Terraform::BIGIP::SysDns

`bigip_sys_dns` Configures DNS server on F5 BIG-IP

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::BIGIP::SysDns",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#nameservers" title="NameServers">NameServers</a>" : <i>[ String, ... ]</i>,
        "<a href="#numberofdots" title="NumberOfDots">NumberOfDots</a>" : <i>Double</i>,
        "<a href="#search" title="Search">Search</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::BIGIP::SysDns
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#nameservers" title="NameServers">NameServers</a>: <i>
      - String</i>
    <a href="#numberofdots" title="NumberOfDots">NumberOfDots</a>: <i>Double</i>
    <a href="#search" title="Search">Search</a>: <i>
      - String</i>
</pre>

## Properties

#### Description

Provide description for your DNS server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameServers

Name or IP address of the DNS server.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumberOfDots

Configures the number of dots needed in a name before an initial absolute query will be made.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Search

Specify what domains you want to search.

_Required_: No

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

