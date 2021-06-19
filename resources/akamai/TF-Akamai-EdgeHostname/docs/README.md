# TF::Akamai::EdgeHostname

~> **Note** Version 1.0.0 of the Akamai Terraform Provider is now available for the Provisioning module. To upgrade to the new version, you have to update this resource. See the [migration guide](../guides/1.0_migration.md) for details. 

The `akamai_edge_hostname` resource lets you configure a secure edge hostname. Your 
edge hostname determines how requests for your site, app, or content are mapped to 
Akamai edge servers. 

An edge hostname is the CNAME target you use when directing your end user traffic to 
Akamai. Each hostname assigned to a property has a corresponding edge hostname. 
 
Akamai supports three types of edge hostnames, depending on the level of security 
you need for your traffic: Standard TLS, Enhanced TLS, and Shared Certificate. When 
entering the `edge_hostname` attribute, you need to include a specific domain suffix 
for your edge hostname type: 

| Edge hostname type | Domain suffix |
|------|-------|
| Enhanced TLS | edgekey.net |
| Standard TLS | edgesuite.net |
| Shared Cert |...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Akamai::EdgeHostname",
    "Properties" : {
        "<a href="#certificate" title="Certificate">Certificate</a>" : <i>Double</i>,
        "<a href="#contract" title="Contract">Contract</a>" : <i>String</i>,
        "<a href="#contractid" title="ContractId">ContractId</a>" : <i>String</i>,
        "<a href="#edgehostname" title="EdgeHostname">EdgeHostname</a>" : <i>String</i>,
        "<a href="#group" title="Group">Group</a>" : <i>String</i>,
        "<a href="#groupid" title="GroupId">GroupId</a>" : <i>String</i>,
        "<a href="#ipbehavior" title="IpBehavior">IpBehavior</a>" : <i>String</i>,
        "<a href="#product" title="Product">Product</a>" : <i>String</i>,
        "<a href="#productid" title="ProductId">ProductId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Akamai::EdgeHostname
Properties:
    <a href="#certificate" title="Certificate">Certificate</a>: <i>Double</i>
    <a href="#contract" title="Contract">Contract</a>: <i>String</i>
    <a href="#contractid" title="ContractId">ContractId</a>: <i>String</i>
    <a href="#edgehostname" title="EdgeHostname">EdgeHostname</a>: <i>String</i>
    <a href="#group" title="Group">Group</a>: <i>String</i>
    <a href="#groupid" title="GroupId">GroupId</a>: <i>String</i>
    <a href="#ipbehavior" title="IpBehavior">IpBehavior</a>: <i>String</i>
    <a href="#product" title="Product">Product</a>: <i>String</i>
    <a href="#productid" title="ProductId">ProductId</a>: <i>String</i>
</pre>

## Properties

#### Certificate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Contract

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContractId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EdgeHostname

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Group

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpBehavior

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Product

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProductId

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

#### Id

Returns the <code>Id</code> value.

