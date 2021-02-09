#include <stdio.h>
#include <string.h>
#define min(x, y) (x > y) ?: y, x

int main()
{
    int bsize, orate, count = 0, drop = 0, nsec, i = 0, inp[100], ch, x;

    printf("\nEnter bucket size:");
    scanf("%d", &bsize);

    printf("\nEnter bucket output rate: ");
    scanf("%d", &orate);

    do
    {
        printf("\nEnter number of packets arriving at second %d:", i + 1);
        scanf("%d", &inp[i]);
        i++;

        printf("\nEnter 1 to continue or 0 to end....");
        scanf("%d", &ch);
    } while (ch);

    nsec = i;
    printf("\nSecond\tRecieved\tSent\tDropped\tRemaining\n");
    for (i = 0; count || nsec > i; i++)
    {
        printf("\t%d", i + 1);
        printf("\t%d", inp[i]);
        printf("\t%d", min((inp[i] + count), orate));

        if (x = (inp[i] + count - orate) > 0)
        {
            if (x > bsize)
            {
                count = bsize;
                drop = x - bsize;
            }
            else
            {
                count = x;
                drop = 0;
            }
        }
        else
        {
            count = 0;
            drop = 0;
        }
        printf("\t%d\t%d\n", drop, count);
    }
}