# TF::Aviatrix::SegmentationSecurityDomainConnectionPolicy

The **aviatrix_segmentation_security_domain_connection_policy** resource handles creation of [Transit Segmentation](https://docs.aviatrix.com/HowTos/transit_segmentation_faq.html) Security Domain Connection Policies.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::SegmentationSecurityDomainConnectionPolicy",
    "Properties" : {
        "<a href="#domainname1" title="DomainName1">DomainName1</a>" : <i>String</i>,
        "<a href="#domainname2" title="DomainName2">DomainName2</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::SegmentationSecurityDomainConnectionPolicy
Properties:
    <a href="#domainname1" title="DomainName1">DomainName1</a>: <i>String</i>
    <a href="#domainname2" title="DomainName2">DomainName2</a>: <i>String</i>
</pre>

## Properties

#### DomainName1

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainName2

_Required_: Yes

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

